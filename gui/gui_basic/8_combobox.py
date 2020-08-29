import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")

values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.set("카드 결제일")
combobox.pack()

combobox_ro = ttk.Combobox(root, height=10, values=values, state="readonly")
combobox_ro.current(0)  # 0 번째 인덱스값 선택
combobox_ro.pack()


def btncmd():
    print(combobox.get())       # 선택된 값 출력
    print(combobox_ro.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()