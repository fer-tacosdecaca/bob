from tkinter import *
#from PIL import ImageTk

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

direction = ""
oldx=50
oldy=50
newx=50
newy=50

def rw(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy

    oldx = newx
    oldy = newy

    newx = newx + 10
    direction = "right"
    draw(direction, oldx, oldy, newx, newy)

def lw(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy

    oldx = newx
    oldy = newy

    newx = newx - 10
    direction = "left"
    draw(direction, oldx, oldy, newx, newy)

def uw(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy

    oldx = newx
    oldy = newy

    newy = newy -10
    direction = "up"
    draw(direction, oldx, oldy, newx, newy)

def dw(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy

    oldx = newx
    oldy = newy

    newy = newy +10
    direction = "down"
    draw(direction, oldx, oldy, newx, newy)

def draw( direction, oldx, oldy, newx, newy):
    fill_color = input_box.get()

    if(direction=="right"):
        right_line=canvas.create_line(oldx, oldy, newx, newy, width = 3, fill= fill_color)
    if(direction=="left"):
        left_line=canvas.create_line(oldx, oldy, newx, newy, width = 3, fill= fill_color)
    if(direction=="up"):
        left_line=canvas.create_line(oldx, oldy, newx, newy, width = 3, fill= fill_color)
    if(direction=="down"):
        left_line=canvas.create_line(oldx, oldy, newx, newy, width = 3, fill= fill_color)
        


canvas.pack()
root.bind("<Right>",rw)
root.bind("<Left>",lw)
root.bind("<Up>",uw)
root.bind("<Down>",dw)



root.mainloop()