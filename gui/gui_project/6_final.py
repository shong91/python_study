import os
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image

root = Tk()
root.title("GUI project")


#####################################################################################################################################################
# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                        filetypes=(('PNG 파일', '*.png'), ('JPG 파일', '*.jpg'), ('모든 파일', '*.*')),
                                        initialdir=r"D:\Github_repo\python_study\gui_project\images")
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

    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# 이미지 set
def set_image():
    # 가로넓이
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
    else:
        img_space = 0

    # 포맷
    img_format = cmb_format.get().lower()

    return img_width, img_space, img_format


#이미지리스트 set
def set_imagelist(img_width, img_space):
    # 1. 선택한 조건에 맞게 너비,간격,높이 조정
    images = [Image.open(x) for x in list_file.get(0, END)]
    image_sizes = []
    if img_width > -1: # 선택된 너비 사용
        image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
    else: # 원본 이미지 사용
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    print("image_sizes: ", image_sizes)
    widths, heights = zip(*image_sizes)
    print("width: ", widths)
    print("height: ", heights)

    max_width, total_height = max(widths), sum(heights)

    if img_space > 0:
        total_height += (img_space * (len(images) -1))

    result_img = Image.new('RGB', (max_width, total_height), (255, 255, 255))
    y_offset = 0  # 다음 이미지를 붙일 y 좌표

    # 2. 이미지를 하나로 합치기
    for idx, img in enumerate(images):
        if img_width > -1:  # 원본유지가 아닐 경우 이미지 크기 리사이즈
            img = img.resize(image_sizes[idx])

        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_space)

        set_progressbar(idx, images)

    return result_img


# 프로그레스 바 표시
def set_progressbar(idx, images):
        progress = (idx +1) / len(images) * 100
        p_bar.set(progress)
        progress_bar.update()


def save_file(img_format, result_img):
    file_name = "photo." + img_format
    dest_path = os.path.join(txt_dest_path.get(), file_name)
    result_img.save(dest_path)
    msgbox.showinfo('알림', '작업이 완료되었습니다.')


# 이미지 통합
def merge_image():
    try:
        img_width, img_space, img_format = set_image()
        result_img = set_imagelist(img_width, img_space)
        save_file(img_format, result_img)
    except Exception as err:
        msgbox.showerror('에러', err)


# 시작
def start():
    if list_file.size() == 0:
        msgbox.showwarning('경고', '이미지 파일을 추가하세요.')
        return
    elif len(txt_dest_path.get()) == 0:
        msgbox.showwarning('경고', '저장 경로를 추가하세요. ')
        return

    merge_image()


######################################################################################################################################################
# 파일 프레임 #
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, text="파일 추가", width=10, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="파일 삭제", width=10, command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임 #
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)
# 저장 경로 프레임 #
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True)

btn_dest_path = Button(path_frame, text="찾아보기", command=browse_dest_path)
btn_dest_path.pack(side="right")

# 옵션 프레임 #
frame_option = LabelFrame(root, text="옵션")
frame_option.pack()

# 1. 가로 넓이 옵션
# 가로넓이 레이블
lbl_width = Label(frame_option, text="가로 넓이")
lbl_width.pack(side="left")

# 가로넓이 콤보박스
opt_width = ['원본유지', '1024', '800', '640']
cmb_width = ttk.Combobox(frame_option, values=opt_width)
cmb_width.current(0)
cmb_width.pack(side="left")

# 2. 간격 옵션
# 간격옵션 레이블
lbl_space = Label(frame_option, text="간격")
lbl_space.pack(side="left")

# 간격옵션 콤보박스
opt_space = ['없음', '좁게', '보통', '넓게']
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space)
cmb_space.current(0)
cmb_space.pack(side="left")

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷")
lbl_format.pack(side="left")

# 파일 포맷 옵션 콤보박스
opt_format = ['png', 'jpg', 'bmp']
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left")

# 진행 상황 프로그레스 바 프레임 #
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x")

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_bar)
progress_bar.pack(fill="x")

# 실행 프레임 #
frame_run = Frame(root)
frame_run.pack(fill="x")

btn_start = Button(frame_run, text="시작", width=10, command=start)
btn_start.pack(side="right")

btn_close = Button(frame_run, text="종료", width=10, command=root.quit)
btn_close.pack(side="right")

######################################################################################################################################################
root.resizable(False, False)
root.mainloop()