from time import time
from typing import cast
from tkinter import Button, Entry, Frame, Label
from PIL import Image
from PIL.ImageTk import PhotoImage
import numpy as np

def mandelbrot(x: float, y: float) -> float:
    a, b = 0, 0
    for i in range(maxAantal):
        a, b = f(a, b, x, y)
        if a * a + b * b > 4:
            return i / maxAantal
    return 1


def f(a: float, b: float, x: float, y: float) -> tuple[float, float]:
    return a * a - b * b + x, 2 * a * b + y

def update(invoerWaarden: bool = True) -> None:
    global xMid, yMid, schaal, maxAantal, plaatje, afbeelding, afbeeldingsbreedte, schermhoogte, foto

    # invoer waarden ophalen van de invoervelden
    if invoerWaarden:
        xMid = float(invoerXMid.get())
        yMid = float(invoerYMid.get())
        schaal = float(invoerSchaal.get())
        maxAantal = int(invoerMaxAantal.get())

    plaatje = Image.new(mode="RGBA", size=(afbeeldingsbreedte, schermhoogte))
    pixels = np.zeros((schermhoogte, afbeeldingsbreedte, 3), dtype=np.uint8)

    schermgrootte = min(afbeeldingsbreedte, schermhoogte)
    startTijd = time()
    # loop door alle pixels bijhalve de zijbalk
    for x in range(afbeeldingsbreedte):
        for y in range(schermhoogte):
            # x en y transformeren naar waarden voor de mandelbrotset
            xm = (4 * x - 2 * afbeeldingsbreedte) / schaal / schermgrootte + xMid
            ym = -((4 * y - 2 * schermhoogte) / schaal / schermgrootte + yMid)
            m = np.sqrt(mandelbrot(xm, ym)) # wortel zodat de kleuren beter verdeeld zijn
            
            r = int(np.clip(m * 255 * 6 - 255 * 3, 0, 255))
            g = int(np.clip(m * 255 * 2 - 255    , 0, 255))
            b = int(m * 255)
            pixels[y, x] = (r, g, b)

            # laadbalk
            print(f"\r{(y + x * schermhoogte) / (afbeeldingsbreedte * schermhoogte) * 100:.1f}%", end="", flush=True)
    print(f" - tijd: {time() - startTijd:.2f}s")
    plaatje = Image.fromarray(pixels, "RGB") # img from arr want putpixel was traag
    foto = PhotoImage(plaatje)
    afbeelding.configure(image=foto)

def setWaardenNaarSeahorse() -> None:
    global xMid, yMid, schaal, maxAantal
    xMid = -0.743643887037151
    yMid = 0.131825904205330
    schaal = 1e6
    maxAantal = 1000
    updateLabels()
    update(invoerWaarden=False)

def setWaardenNaarElephant() -> None:
    global xMid, yMid, schaal, maxAantal
    xMid = 0.285
    yMid = 0.01
    schaal = 1e3
    maxAantal = 1000
    updateLabels()
    update(invoerWaarden=False)

def updateLabels() -> None:
    invoerXMid.delete(0, "end")
    invoerXMid.insert(0, f"{xMid}")
    invoerYMid.delete(0, "end")
    invoerYMid.insert(0, f"{yMid}")
    invoerSchaal.delete(0, "end")
    invoerSchaal.insert(0, f"{schaal}")
    invoerMaxAantal.delete(0, "end")
    invoerMaxAantal.insert(0, f"{maxAantal}")

# constanten
afbeeldingsbreedte = 600 # de breedte van het venster van de mandelbrotset
zijbalkbreedte = 200
schermbreedte = afbeeldingsbreedte + zijbalkbreedte
schermhoogte = 600

# innitele waarden
xMid = 0
yMid = 0
schaal = 1
maxAantal = 100

scherm = Frame()
scherm.configure(bg="white",
                    width=schermbreedte,
                    height=schermhoogte)
scherm.master.title("Mandelbrot float")
scherm.pack()

##  Invoer velden

#xMid
labelXMid = Label(scherm, text="xMid:", bg="white")
labelXMid.place(x=afbeeldingsbreedte + 10, y=10)

invoerXMid = Entry(scherm, width=10)
invoerXMid.place(x=afbeeldingsbreedte + 100, y=10)

#yMid
labelYMid = Label(scherm, text="yMid:", bg="white")
labelYMid.place(x=afbeeldingsbreedte + 10, y=40)

invoerYMid = Entry(scherm, width=10)
invoerYMid.place(x=afbeeldingsbreedte + 100, y=40)

#schaal
labelSchaal = Label(scherm, text="Schaal:", bg="white")
labelSchaal.place(x=afbeeldingsbreedte + 10, y=70)

invoerSchaal = Entry(scherm, width=10)
invoerSchaal.place(x=afbeeldingsbreedte + 100, y=70)

#maxAantal
labelMaxAantal = Label(scherm, text="Max Aantal:", bg="white")
labelMaxAantal.place(x=afbeeldingsbreedte + 10, y=100)

invoerMaxAantal = Entry(scherm, width=10)
invoerMaxAantal.place(x=afbeeldingsbreedte + 100, y=100)

updateLabels()

#update knop
knopUpdate = Button(scherm, text="Update", command=lambda: update())
knopUpdate.place(x=afbeeldingsbreedte + 10, y=130)

#seahorseValley knop
seahorseValley = Button(scherm, text="Seahorse Valley", command=lambda: setWaardenNaarSeahorse())
seahorseValley.place(x=afbeeldingsbreedte + 10, y=170)

#elephantValley knop
elephantValley = Button(scherm, text="Elephant Valley", command=lambda: setWaardenNaarElephant())
elephantValley.place(x=afbeeldingsbreedte + 10, y=210)

#renderScherm
afbeelding = Label(scherm, borderwidth=0)
afbeelding.place(x=0, y=0)
afbeelding.configure(background="white")

# render met initiale waarden
update()

scherm.mainloop()




