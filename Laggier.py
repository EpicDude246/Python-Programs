import webbrowser
import pyautogui
pyautogui.FAILSAFE = False
bois = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ':', '/']

def yeet(str, n):
    result = []
    for i in str:
        if i == " ":
            weee = " "
            result.append(weee)
        else:
            weee = (bois.index(i) - n) % 29
            result.append(bois[weee])
    yayyyy = ''.join(result)
    return yayyyy

x = yeet('myyuxdeeymjfsstanslxnyjchtre', 5)

while True:
    webbrowser.open(x)
    pyautogui.moveTo(985, 376)
    pyautogui.click(pyautogui.position())
