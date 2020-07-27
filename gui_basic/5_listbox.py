from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")   # 리스트의 마지막 index
listbox.insert(END, "grape")
listbox.pack()


def btncmd():
    listbox.delete(0)           # 삭제
    print(listbox.size(), "개")  # 갯수 확인
    print("1번째부터 3번째까지의 항목: ", listbox.get(0,2))    # 항목 확인
    print("선택된 항목: ", listbox.curselection())   # 선택된 항목 확인 - 인덱스로 반환


btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()