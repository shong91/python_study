from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")

chkvar = IntVar()   # chkvar에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="remind me later", variable=chkvar)
chkbox.select()
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="never show again", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) # 0: 체크해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()