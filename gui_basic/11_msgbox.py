import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI basic")
root.geometry("640x480+700+100")


# 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 되었습니다. ")


def warn():
    msgbox.showwarning("경고", "이미 선택된 좌석입니다. ")


def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다. ")


def okcancel():
    msgbox.askokcancel("확인/취소", "해당 좌석을 예매하시겠습니까? ")


def retrycancel():
    msgbox.askretrycancel("재시도/취소", "일시적 오류가 발생했습니다. 재시도 하겠습니까? ")


def yesno():
    msgbox.askyesno("예/아니오", "해당 좌석을 예매하시겠습니까? ")


def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하시겠습니까? ")
    # 네: 저장 후 종료
    # 아니오: 저장 하지 않고 종료
    # 취소: 프로그램 종료 취소
    print("응답: ", response)
    if response == 1:
        print("YES")
    elif response == 0:
        print("NOOOO")
    else:
        print("CANCEL")


Button(root, command=info, text="alart").pack()
Button(root, command=warn, text="warn").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="ok/cancel").pack()
Button(root, command=retrycancel, text="retry/cancel").pack()
Button(root, command=yesno, text="yes/no").pack()
Button(root, command=yesnocancel, text="yes/no/cancel").pack()


root.mainloop()
