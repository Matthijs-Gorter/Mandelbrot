from typing import cast
from tkinter import Toplevel, Frame, Label
from PIL import Image, ImageDraw
from PIL.ImageTk import PhotoImage

def mandelbrot(x,y):
    return x + y

scherm = Frame()
scherm.configure(bg="white",
                    width=500,
                    height=500)
scherm.master.title("Mandelbrot float")
scherm.pack()

plaatje = Image.new(mode="RGBA", size=(500, 500))

for x in range(500):
    for y in range(500):
        kleur = int(mandelbrot(x, y) / 4)
        plaatje.putpixel((x,y), (255 - kleur, kleur, kleur, 255))

afbeelding = Label(scherm, borderwidth=0)
afbeelding.place(x=0, y=0)
afbeelding.configure(background="white")

foto = PhotoImage(plaatje)
afbeelding.configure(image=foto)

scherm.mainloop()




