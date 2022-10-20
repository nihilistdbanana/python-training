import time
from tkinter import*
root=Tk()
root.geometry("350x150+0+0") # The geometry used to define clock size
root.configure(background = "Black") # clock background color
root.resizable(0,0)  # no one can resize of clock
root.overrideredirect(1) # To Hide tkinter heading
def start():
    text= time.strftime("%H:%M:%S")
    label.configure(text=text)
    label.after(200,start)

label= Label(root,font=("ds-digital",50,'bold'),bg='Black',fg='red',bd=50)
# Font colour,size
label.grid(row=0,column=1)
start()
print("done")
root.mainloop()
