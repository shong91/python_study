import os
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image

root = Tk()
root.title("GUI project")
##############################################################################################ㅣ
# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                        filetypes=(("PNG 파일", "*.png"),("모든 파일", "*.*")),
                                        initialdir=r"D:\Github_repo\python_study\gui_project\images")
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


# 파일 삭제
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장 경로 - 출력 폴더 선택
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    print(folder_selected)

    txt_dest_path.delete(0, END) # 앞서 값이 있었다면 먼저 지워준다
    txt_dest_path.insert(0, folder_selected)


# 이미지 통합
def merge_image():
    try:
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width == '원본유지':
            img_width = -1
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == '좁게':
            img_space = 30
        elif img_space == '보통':
            img_space = 60
        elif img_space == '넓게':
            img_space = 90
        else:           # '없음'
            img_space = 0

        img_format = cmb_format.get().lower()

        ###############################################################
        print(list_file.get(0, END))
        images = [Image.open(x) for x in list_file.get(0,END)]

        # 이미지 사이즈를 tuple 로 받아 list 로 저장
        image_sizes = []
        if img_width > -1:
            # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]
        # 높이 계산
        # 원본 width(x) : 원본 height(y) = 변경 width(x') : 변경 height(y')
        # xy' = x'y
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width
        # y' = x'y / x = img_width * size[1] / size[0]

        #[(10,10), (20,20), (30,30)]
        print('-------------------------------------------------------')
        print(image_sizes)
        widths, heights = zip(*image_sizes)

        print("width: ", widths)
        print("height: ", heights)

        max_width, total_height = max(widths), sum(heights)
        print("maxW: ", max_width)
        print("sumH: ", total_height)

        # 이미지 간격 옵션 적용
        if img_space > 0:
            total_height += (img_space * (len(images) -1))

        # 스케치북 준비
        result_img = Image.new("RGB", (max_width, total_height), (255,255,255))
        y_offset = 0 # 다음 이미지를 붙일 y 위치 정보

        for idx, img in enumerate(images):
            # width 가 원본유지가 아닐 경우 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx+1) / len(images) * 100
            p_bar.set(progress)
            progress_bar.update()

        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1]

        # 포맷 옵션 처리
        file_name = "photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다. ")
    except Exception as err:
        msgbox.showerror('에러', err)

# 시작
def start():
    print("가로넓이: ", cmb_width.get())
    print("간격: ", cmb_space.get())
    print("포맷: ", cmb_format.get())

    # 파일 목록 / 저장 경로 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    elif len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 추가하세요")
        return

    merge_image()


##############################################################################################
# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="add File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="delete File", command=del_file)
btn_del_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

# 저장 경로
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x",padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)


# 2. 간격 옵션
# 간격옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격옵션 콤보박스
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보박스
opt_format = ["png", "jpg", "bmp"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진행 상황 프로그레스 바
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_bar)
progress_bar.pack(fill="x", padx=5, pady=5)


# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_start = Button(frame_run, text="시작", padx=5, pady=5, width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

btn_close = Button(frame_run, text="닫기", padx=5, pady=5, width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()