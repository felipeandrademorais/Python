import pyautogui

# Writer (967,713)
# Sender (1248, 708)

msg = "Mensagem a ser enviada"

pyautogui.click(967, 713)
pyautogui.typewrite(msg, interval=0.1)
pyautogui.click(1248, 708)