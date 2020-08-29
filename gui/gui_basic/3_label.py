from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480")

# 레이블은 글자/이미지만을 보여줌 (이벤트 X)
label1 = Label(root, text="hello!")
label1.pack()

photo = PhotoImage(file="image.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="bye~")
    
    # 지역변수로 선언할 경우, GC가 돌면서 photo2를 쓰레기 값으로 인지하여 GUI에 출력되지 않게 됨
    # => 전역변수로 선언하여야 함
    global photo2
    photo2 = PhotoImage(file="image2.png")
    label2.config(image=photo2)


btn = Button(root, text="click", command=change)
btn.pack()
root.mainloop()