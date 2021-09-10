"""
직접 원하는 위치 잡아서 캡쳐 
최종 수정일자 :21.09.11


# 설치방법
# py -m pip install pyautogui
"""


import time


import pyautogui as pygui

pygui.hotkey('alt', 'tab')
print("3초뒤 좌측 위 마우스 위치를 입력합니다.")
time.sleep(3)
leftup_position = pygui.position()
print(leftup_position)

pygui.hotkey('alt', 'tab')
time.sleep(0.5)
pygui.hotkey('alt', 'tab')

print("3초뒤 우측 아래 마우스 위치를 입력합니다.")
time.sleep(3)
rightdown_position = pygui.position()
print(rightdown_position)

# file_dir='./'
pygui.hotkey('alt', 'tab')

startpage = 0
endpage = 0
startpage = int(input("시작페이지 입력하시오 : "))
endpage = int(input("종료 페이지 : "))

pygui.hotkey('alt', 'tab')
time.sleep(1)
pygui.click(rightdown_position.x-20, rightdown_position.y-20)

for index in range(startpage, endpage+1):
    filename = str(index)+".png"
    print(filename)
    # pygui.moveTo(10, 0)

    # 스크린샷
    pygui.screenshot(filename,
                     (leftup_position.x,
                      leftup_position.y,
                      rightdown_position.x-300,
                      rightdown_position.y-300))

    time.sleep(1)
    pygui.press('right')
