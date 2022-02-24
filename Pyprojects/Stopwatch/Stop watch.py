import tkinter as tk
import datetime

counter = datetime.datetime.now()
laps = []
Go = False


def main():
    global Go, l1, clock
    if Go:
        dif = datetime.datetime.now() - counter
        clock=('0' + str(dif))[:-3]
        l1.config(text=f"{clock}", fg='grey')
        bstrt.config(state='disabled')
        bstpt.config(state='normal')
        l1.after(1, main)            #after works on root or widgets, pass in timedelay in ms and a func to be executed
                    # when the time has passed .The after callback is only called once for each call to this method.
                    # To keep calling the callback, you need to register the callback inside itself


def start():
    global Go
    Go = True
    main()
    blaps.config(state='normal')
    brst.config(state='normal')

def stop():
    global Go
    Go = False
    bstrt.config(state='normal')
    bstpt.config(state='disabled')
    brst.config(state='normal')
    blaps.config(state='disabled')

def reset():
    global counter, l1, laps
    counter = datetime.datetime.now()
    l1.config(text=f"{strt}", fg='black')
    for i in range(len(laps)):
        laps[i].destroy()
    laps=[]

def lap():
    global laps
    laps.append(tk.Label(text=f"lap{len(laps)+1}: {clock}", font=("Courier", 12)))
    laps[len(laps)-1].place(x=100, y=140 + len(laps) * 20)

root = tk.Tk()
root.title('Stop watch')
root.geometry('400x400')
root.iconbitmap(r'stopwatch.ico')

strt = datetime.time(0,0,0,0).strftime('%H:%M:%S.%f')
strt = strt[:-3]       # shows only 3 decimals
l1 = tk.Label(root, text=strt, font=("Courier", 30), relief='sunken', pady=30, bg='white', borderwidth=8)
l1.pack(side='top')


frame = tk.Frame(root)
frame.pack(anchor='center')

bstrt = tk.Button(frame, text='Start', command=start)
bstpt = tk.Button(frame, text='Stop', command=stop, state='disabled')
brst = tk.Button(frame, text='Reset', command=reset, state='disabled')
blaps = tk.Button(frame, text='Lap', command=lap, state='disabled')
bstrt.pack(side='left')
bstpt.pack(side='left')
brst.pack(side='left')
blaps.pack(side='left')

root.mainloop()



