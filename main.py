from tkinter import *

window = Tk()
window.geometry('550x400')
window.title('Color picker')


# window.resizable(False, False)


def color_generate(value):
    redg = red.get()
    greeng = green.get()
    blueg = blue.get()
    color = f'#{redg:02x}{greeng:02x}{blueg:02x}'
    labelcolor.configure(bg=color, text=color)
    red2 = 255 - red.get()
    green2 = 255 - green.get()
    blue2 = 255 - blue.get()
    color2 = f'#{red2:02x}{green2:02x}{blue2:02x}'
    labelcolor.configure(fg=color2)
    copypaste.delete(0, END)
    copypaste.insert(END, color)


ru = ['Выберите цвета', 'Результат', 'Красный', 'Зелёный', 'Синий', 'Языки', 'Темы', 'Обычная', 'Тёмная']
en = ['Choose the colors', 'Result', 'Red', 'Green', 'Blue', 'Languages', 'Themes', 'Normal', 'Dark']


def language():
    if var.get() == 1:
        frameRGB.configure(text=en[0])
        framecolor.configure(text=en[1])
        red.configure(label=en[2])
        green.configure(label=en[3])
        blue.configure(label=en[4])
        languages.configure(text=en[5])
        themes.configure(text=en[6])
        L1.configure(text=en[7])
        L2.configure(text=en[8])

    else:
        frameRGB.configure(text=ru[0])
        framecolor.configure(text=ru[1])
        red.configure(label=ru[2])
        green.configure(label=ru[3])
        blue.configure(label=ru[4])
        languages.configure(text=ru[5])
        themes.configure(text=ru[6])
        L1.configure(text=ru[7])
        L2.configure(text=ru[8])


def theme():
    if var2.get() == 2:
        window.configure(bg='#36393F')
        languages.configure(bg='#36393F', fg='white')
        themes.configure(bg='#36393F', fg='white')
        frameRGB.configure(bg='#36393F', fg='white')
        framecolor.configure(bg='#36393F', fg='white')
        red.configure(bg='#2F3136')
        green.configure(bg='#2F3136')
        blue.configure(bg='#2F3136')
        R1.configure(bg='#36393F', fg='white')
        R2.configure(bg='#36393F', fg='white')
        L1.configure(bg='#36393F', fg='white')
        L2.configure(bg='#36393F', fg='white')
    else:
        window.configure(bg='SystemButtonFace')
        languages.configure(bg='SystemButtonFace', fg='black')
        themes.configure(bg='SystemButtonFace', fg='black')
        frameRGB.configure(bg='SystemButtonFace', fg='black')
        framecolor.configure(bg='SystemButtonFace', fg='black')
        red.configure(bg='SystemButtonFace')
        green.configure(bg='SystemButtonFace')
        blue.configure(bg='SystemButtonFace')
        R1.configure(bg='SystemButtonFace', fg='black')
        R2.configure(bg='SystemButtonFace', fg='black')
        L1.configure(bg='SystemButtonFace', fg='black')
        L2.configure(bg='SystemButtonFace', fg='black')


frameRGB = LabelFrame(text='Choose the colors', height=250, width=250)
framecolor = LabelFrame(text='Result', height=250, width=250)
copypaste = Entry(framecolor, justify=CENTER)
labelcolor = Label(framecolor, text='#000000', bg='black', fg='white', font=('Arial', 15, 'bold'), height=6, width=16)
red = Scale(frameRGB, length=200, width=20, command=color_generate, to=255, orient=HORIZONTAL, label='Red',
            fg='red', activebackground='red')
green = Scale(frameRGB, length=200, width=20, command=color_generate, to=255, orient=HORIZONTAL, label='Green',
              fg='green', activebackground='green')
blue = Scale(frameRGB, length=200, width=20, command=color_generate, to=255, orient=HORIZONTAL, label='Blue',
             fg='blue', activebackground='blue')
frameRGB.grid(row=0, column=0, padx=14, pady=20)
framecolor.grid(row=0, column=1, padx=10, pady=20)
labelcolor.pack(padx=17, pady=12)
red.grid(row=0, column=0, padx=25, pady=7)
green.grid(row=1, column=0, padx=15, pady=6)
blue.grid(row=2, column=0, padx=15, pady=6)
copypaste.pack(pady=17)

var = IntVar()
languages = LabelFrame(text='Languages', height=100, width=250)
R1 = Radiobutton(languages, text="English", variable=var, value=1,
                 command=language)
R2 = Radiobutton(languages, text="Русский", variable=var, value=2,
                 command=language)
R1.select()
R1.pack(padx=91, pady=3)
R2.pack(padx=91, pady=3)

languages.grid(row=1, column=0, padx=10, pady=20)

var2 = IntVar()
themes = LabelFrame(text='Themes', height=100, width=250)
L1 = Radiobutton(themes, text="Normal", variable=var2, value=1,
                 command=theme)
L2 = Radiobutton(themes, text="Dark", variable=var2, value=2,
                 command=theme)
L1.select()
L1.pack(padx=82, pady=3)
L2.pack(padx=82, pady=3)

themes.grid(row=1, column=1, padx=10, pady=20)

window.mainloop()
