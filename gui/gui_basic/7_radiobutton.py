from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")

Label(root, text="select menu").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenburger", value=3, variable=burger_var)
btn_burger1.select()

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select drinks").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="cola", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="cider", value="사이다", variable=drink_var)

btn_drink1.select()
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get()) # 선택된 라디오버튼 항목의 값(value) 을 반환
    print(drink_var.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()