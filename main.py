from pynput import keyboard
import clipboard
import pyttsx3

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='s'), keyboard.KeyCode(char='t')},
    {keyboard.Key.ctrl, keyboard.KeyCode(char='S'), keyboard.KeyCode(char='T')}
]

# The currently active modifiers
engine = pyttsx3.init()
current = set()
cont = keyboard.Controller()

def execute():
    print("function activated!")
    cont.press(keyboard.Key.ctrl)
    cont.press(keyboard.KeyCode(char='c'))
    time.sleep(0.25)
    cont.release(keyboard.Key.ctrl)
    cont.release(keyboard.KeyCode(char='c'))
    engine.runAndWait()
    content = clipboard.paste()
    engine.say(content)


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            current.add(k)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                execute()
    
    else:
        print("you didn't typed it write")

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
