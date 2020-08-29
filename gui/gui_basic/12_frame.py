import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+700+100")

Label(root, text="메뉴를 선택해주세요.").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")
# 키오스크 주문
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="burger").pack()
Button(frame_burger, text="cheeseburger").pack()
Button(frame_burger, text="chickenburger").pack()

frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="color").pack()
Button(frame_drink, text="cider").pack()

root.mainloop()
