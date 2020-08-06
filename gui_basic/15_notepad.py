import os
from tkinter import *

root = Tk()
root.title("Windows Notepad")
root.geometry("640x480+500+100")

# 파일명
filename="mynote.txt"


def openFile():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="UTF-8") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())

2
def saveFile():
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text.get("1.0", END))


#메뉴 영역
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=openFile)
menu_file.add_command(label="Save", command=saveFile)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu_template= Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)

menu.add_cascade(label="Edit")
menu.add_cascade(label="Template")
menu.add_cascade(label="View", menu=menu_view)
menu.add_cascade(label="Help", menu=menu_help)

# 본문 영역
scroll = Scrollbar(root)
text = Text(root, yscrollcommand=scroll.set)
text.pack(side="left", fill="both", expand=True)

# 스크롤바
scroll.pack(side="right", fill="y")
scroll.config(command=text.yview)

root.config(menu=menu)
root.mainloop()