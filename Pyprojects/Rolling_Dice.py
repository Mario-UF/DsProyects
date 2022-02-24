import random
import tkinter as tk

# rolling()

# Add a GUI (Graphical user interface) with tkinter library

root = tk.Tk()
root.geometry('380x400')

# --Label Frame
lb = tk.LabelFrame(root, text='Number of faces', width=150, height=150) #, padx=5, pady=50)
lb.place(x=20, y=30)
lb.pack_propagate(False)      # this allows us to fix the widget depending on the child widgets (.grid_propagate(False))

# --Combobox
dice_faces = [i for i in range(4, 17)]     # we define 4 and 16 as the min and max number of faces respectively
var = tk.IntVar()
var.set('select the number')
df = tk.OptionMenu(lb, var, *dice_faces)
df.pack()

# --Label Frame2
lb2 = tk.LabelFrame(root, text='Number of dices', padx=55, pady=3)
lb2.place(x=200, y=30)

# --Radiobutton
dice_number = [i for i in range(1,6)]
var2 = tk.IntVar()
for i in range(5):
    tk.Radiobutton(lb2, var=var2, text=dice_number[i], value=dice_number[i]).pack()

output_labl = tk.Label(root)

labels = []
def rolling():
    global labels
    # for i in range(len(labels)):        # this is another way to delete the labels using a for loop to destroy the
    #     labels[i].destroy()               # elements and then redefine the list to have no empty elements inside
    # labels = []

    while labels:
        removed_element = labels.pop(0)
        removed_element.destroy()

    for i in range(1,var2.get()+1):
        r = random.choice([i for i in range(1,var.get())])
        labels.append(tk.Label(root, text=f"The dice {i} shows: {r}"))
        labels[i-1].place(x=140, y=240+i*20)


button = tk.Button(root, text="Let's roll", command=rolling, padx=20, pady=5)
button.place(x=140, y=205)

root.mainloop()
