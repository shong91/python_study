from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")

txt = Text(root, width=20, height=5) # 엔터 가능
txt.pack()
txt.insert(END, "insert data")

e = Entry(root, width=30) # 엔터 불가
e.pack()
e.insert(0, "insert 1 row")


def btncmd():
    print(txt.get("1.0", END)) # 처음(라인 1.0)부터 끝(컬럼기준 END번쨰)까지 있는 모든 데이터
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()