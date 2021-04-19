
'''



# pip install pynput
from pynput.keyboard import Key, Controller
from pynput import keyboard



from pynput.mouse import Button, Controller

mouse = Controller()   #controlar mouse

# Read pointer position
print('posicion {0}'.format(mouse.position))

mouse.position = (10, 20)# Set pointer position

mouse.move(5, -5)# Move pointer relative to current position

mouse.press(Button.left)# Press and release
mouse.release(Button.left)

mouse.click(Button.left, 2)# Double click

mouse.scroll(0, 2)# Scroll two steps down


keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')

# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

# Type 'Hello World' using the shortcut type method
keyboard.type('Hello World')


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()



'''