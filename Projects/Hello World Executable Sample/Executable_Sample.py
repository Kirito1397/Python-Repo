import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

"""""
Learn from "https://datatofish.com/executable-pyinstaller/"

To set custom add an icon to your exe file by using the command
1. Convert image into .ico
2. Save image in the same directory where the .py file is located.
3. pyinstalled --onefile --windowed --icon=icon.ico gui_exe.py


###  To generate an executabe file, with custom icon and avoiding trigerring CMD window first use below command

"pyinstaller --onefile --windowed --icon=Executable_Sample_icon.ico -w Executable_Sample.py"

"""