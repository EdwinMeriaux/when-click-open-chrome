from pynput.mouse import Listener
import logging
import webbrowser

#logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
url = 'www.google.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        
        webbrowser.get(chrome_path).open_new(url)

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
