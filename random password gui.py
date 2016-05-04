

from __future__ import print_function
import Tkinter
import tkFont
import sys
import subprocess
import random
import os


def valid_pass(test_password, all_symbols):
    return all(set(test_password) & set(x) for x in all_symbols)

def get_password():
    length = 16

    all_symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZ',\
                  'abcdefghjklmnpqrstuvwxyz',\
                  '23456789!@#$%^&*'




    if length < len(all_symbols):
        raise ValueError('must be at least {}'
                         ' characters long!'.format(len(all_symbols)))
    new_password = ''
    while not valid_pass(new_password, all_symbols):
        new_password = ''.join(random.choice(''.join(all_symbols))
                               for _ in xrange(length))

    return new_password


def secure_delete(path, passes=1):
    random.seed()
    with open(path, 'ab') as delfile:
        length = delfile.tell()
        for _ in xrange(passes):
            delfile.seek(0)
            for _ in xrange(length):
                delfile.write(str(random.randrange(256)))

    os.remove(path)

def update_password(field):
    field.delete(0, Tkinter.END)
    field.insert(0, get_password())


def main():
    top = Tkinter.Tk()
    top.title('Password generator')

    monospace_font = tkFont.Font(family='monospace', size=16)


    password_label = Tkinter.Label(text='Password:')
    password_label.grid(row=1, column=0)

    password_entry = Tkinter.Entry(top, font=monospace_font)
    password_entry.grid(row=1, column=1)


    button_update_password = Tkinter.Button(top,
                                            text='Generate New Password',
                                            command=
                                            lambda:
                                            update_password(password_entry))
    button_update_password.grid(row=1, column=2)

    size_label = Tkinter.Label(text='Size:')
    size_label.grid(row=3, column=0)

    size_entry = Tkinter.Entry(top, font=monospace_font)
    size_entry.grid(row=3, column=1)

    update_password(password_entry)

    top.mainloop()

if __name__ == '__main__':
    main()