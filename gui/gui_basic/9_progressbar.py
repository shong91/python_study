import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")    # mode = indeterminate / determinate
# progressbar.start(10)       # 10ms 마다 움직임
# progressbar.pack()
#
#
# def btncmd():
#     progressbar.stop()


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd():
    for i in range(1, 101):
        time.sleep(0.01)
        p_var2.set(i)           # 프로그레스바 값 설정
        progressbar2.update()   # UI 업데이트
        print(p_var2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()