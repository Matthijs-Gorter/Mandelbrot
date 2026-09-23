from typing import cast
from tkinter import Toplevel, Frame, Label
from PIL import Image, ImageDraw
from PIL.ImageTk import PhotoImage

def mandelbrot(x: float, y: float) -> int:
    a, b = 0, 0
    for i in range(100):
        a, b = f(a, b, x, y)
        if a * a + b * b > 4:
            return i
    return 100


def f(a: float, b: float, x: float, y: float) -> tuple[float, float]:
    return a * a - b * b + x, 2 * a * b + y

scherm = Frame()
scherm.configure(bg="white",
                    width=800,
                    height=800)
scherm.master.title("Mandelbrot float")
scherm.pack()

plaatje = Image.new(mode="RGBA", size=(800, 800))

for x in range(800):
    for y in range(800):
        kleurR = int(max(mandelbrot(x / 800, y / 800)* 2.55 * 3 - 2.55 * 2, 0))
        kleurG = int(max(mandelbrot(x / 800, y / 800)* 2.55 * 2 - 2.55, 0))
        kleurB = int(mandelbrot(x / 800, y / 800))
        plaatje.putpixel((x,y), (kleurR, kleurG, kleurB, 255))

afbeelding = Label(scherm, borderwidth=0)
afbeelding.place(x=0, y=0)
afbeelding.configure(background="white")

foto = PhotoImage(plaatje)
afbeelding.configure(image=foto)

scherm.mainloop()




