import keyboard
import time
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

# 'ctrl+shift+s' 와 같은 것도 가능
keyboard.add_hotkey('F9', screenshot) # f9 키 누르면 screenshot 함수 실행
keyboard.wait("esc") # esc 키를 누를 때까지 상기의 프로그램 수행