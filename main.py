from time import time
from typing import cast
from tkinter import Button, Entry, Frame, Label
from PIL import Image
from PIL.ImageTk import PhotoImage
import numpy as np

def mandelbrot(x: float, y: float) -> float:
    a, b = 0, 0
    for i in range(max_aantal):
        a, b = f(a, b, x, y)
        if a * a + b * b > 4:
            return i / max_aantal
    return 1


def f(a: float, b: float, x: float, y: float) -> tuple[float, float]:
    return a * a - b * b + x, 2 * a * b + y

def update():
    global xMid, yMid, schaal, max_aantal, plaatje, afbeelding, speelbreedte, schermhoogte, foto

    # invoer waarden ophalen van de invoervelden
    xMid = float(invoerXMid.get())
    yMid = float(invoerYMid.get())
    schaal = float(invoerSchaal.get())
    max_aantal = int(invoerMaxAantal.get())

    plaatje = Image.new(mode="RGBA", size=(speelbreedte, schermhoogte))
    pixels = np.zeros((schermhoogte, speelbreedte, 3), dtype=np.uint8)

    schermgrootte = min(speelbreedte, schermhoogte)
    startTijd = time()
    # loop door alle pixels bijhalve de zijbalk
    for x in range(speelbreedte):
        for y in range(schermhoogte):
            # x en y transformeren naar waarden voor de mandelbrotset
            xm = (4 * x - 2 * speelbreedte) / schaal / schermgrootte + xMid
            ym = (4 * y - 2 * schermhoogte) / schaal / schermgrootte - yMid
            m = np.sqrt(mandelbrot(xm, ym)) # wortel zodat de kleuren beter verdeeld zijn
            
            r = int(np.clip(m * 255 * 6 - 255 * 3, 0, 255))
            g = int(np.clip(m * 255 * 2 - 255    , 0, 255))
            b = int(m * 255)
            pixels[y, x] = (r, g, b)

            # laadbalk
            print(f"\r{(y + x * speelbreedte) / (speelbreedte * schermhoogte) * 100:.1f}%", end="", flush=True)
    print(f" - tijd: {time() - startTijd:.2f}s")
    plaatje = Image.fromarray(pixels, "RGB") # img from arr want putpixel was traag
    foto = PhotoImage(plaatje)
    afbeelding.configure(image=foto)


# constanten
speelbreedte = 600 # de breedte van het venster van de mandelbrotset
zijbalkbreedte = 200
schermbreedte = speelbreedte + zijbalkbreedte
schermhoogte = 600

# innitele waarden
xMid = 0
yMid = 0
schaal = 1
max_aantal = 100

scherm = Frame()
scherm.configure(bg="white",
                    width=schermbreedte,
                    height=schermhoogte)
scherm.master.title("Mandelbrot float")
scherm.pack()

##  Invoer velden 

#xMid
labelXMid = Label(scherm, text="xMid:", bg="white")
labelXMid.place(x=speelbreedte + 10, y=10)

invoerXMid = Entry(scherm, width=10)
invoerXMid.insert(0, f"{xMid}")
invoerXMid.place(x=speelbreedte + 100, y=10)

#yMid
labelYMid = Label(scherm, text="yMid:", bg="white")
labelYMid.place(x=speelbreedte + 10, y=40)

invoerYMid = Entry(scherm, width=10)
invoerYMid.insert(0, f"{yMid}")
invoerYMid.place(x=speelbreedte + 100, y=40)

#schaal
labelSchaal = Label(scherm, text="Schaal:", bg="white")
labelSchaal.place(x=speelbreedte + 10, y=70)

invoerSchaal = Entry(scherm, width=10)
invoerSchaal.insert(0, f"{schaal}")
invoerSchaal.place(x=speelbreedte + 100, y=70)

#max_aantal
labelMaxAantal = Label(scherm, text="Max Aantal:", bg="white")
labelMaxAantal.place(x=speelbreedte + 10, y=100)

invoerMaxAantal = Entry(scherm, width=10)
invoerMaxAantal.insert(0, f"{max_aantal}")
invoerMaxAantal.place(x=speelbreedte + 100, y=100)

#update button
knopUpdate = Button(scherm, text="Update", command=lambda: update())
knopUpdate.place(x=speelbreedte + 10, y=130)

#renderScherm
afbeelding = Label(scherm, borderwidth=0)
afbeelding.place(x=0, y=0)
afbeelding.configure(background="white")

# render met initiale waarden
update()

scherm.mainloop()




