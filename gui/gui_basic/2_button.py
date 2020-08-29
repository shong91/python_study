from tkinter import *

root = Tk()
root.title("GUI basic")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, text="button222222", padx=5, pady=10)       # padx,pady 는 여백
btn2.pack()

btn3 = Button(root, text="button3", padx=10, pady=5)
btn3.pack()

btn4 = Button(root, text="button4444444444", width=10, height=3)    #width/height 고정크기
btn4.pack()

btn5 = Button(root, text="button5", fg="red", bg="yellow")
btn5.pack()

photo = PhotoImage(file="image.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("clicked! ")


btn7 = Button(root, text="버튼이벤트", command=btncmd)
btn7.pack()

root.mainloop()