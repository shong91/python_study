import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+300+100")


def create_new_file():
    print("new file")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)


# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 (radiobutton)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="c++")

menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 (checkbox)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")

menu.add_cascade(label="View", menu=menu_view)




root.config(menu=menu)

root.mainloop()