from tkinter import *
from PIL import ImageTk

root= Tk()
root.title("Trabajar en el lienzo usando funciones")
root.geometry("600x600")

label=Label(root, text="Ingresa un Color :")
label.place(relx=0.6,rely=0.9, anchor= CENTER)
input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx=0.8,rely=0.9, anchor= CENTER)
canvas = Canvas(root, width=580, height=510, bg="white",highlightbackground="lightgray")
#img = ImageTk.PhotoImage(Image.open("start_point.png"))
#my_image = canvas.create_image(50,50,image=img)
canvas.pack()

root.mainloop()