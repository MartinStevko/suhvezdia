import tkinter as tk
import random

SUBORY = [
    'velky_voz',
    'velka_medvedica',
    'leo',
    'kasiopea',
    'blizenci',
    'orion',
    'orol',
    'rak',
    'trojuholnik',
]

subor = 'data/' + random.choice(SUBORY) + '.txt'

print('Použitý bol súbor - ' + subor)

pouzite = []
suradnice = []
try:
    with open(subor, 'r') as f:
        for line in f:
            x, y = line.split()
            suradnice.append([int(x), int(y)])
except:
    print('Chyba, súbor neexistuje!')


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.kresli = tk.Button(self)
        self.kresli["text"] = "Ďalšia čiara"
        self.kresli["command"] = self.new_line
        self.kresli.pack(side="top")

        self.quit = tk.Button(
            self, text="Ukonči",
            fg="red",
            command=root.destroy
        )
        self.quit.pack(side="bottom")

    def new_line(self):
        if len(suradnice) > 1:
            x1 = suradnice[0][0]
            y1 = suradnice[0][1]
            x2 = suradnice[1][0]
            y2 = suradnice[1][1]

            arr = [x1, y1, x2, y2]
            arr2 = [x2, y2, x1, y1]

            if arr2 in pouzite:
                del suradnice[0]
                self.new_line()
            else:
                del suradnice[0]
                pouzite.append(arr)
                canvas.create_line(x1, y1, x2, y2, fill="#ffffff", width='3')
        else:
            print('Došli čiary!')

root = tk.Tk()
root.title = 'Súhvezdia'

canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.pack()

for s in suradnice:
    canvas.create_oval(s[0]-5, s[1]-5, s[0]+5, s[1]+5, fill="#ffffff")

app = App(master=root)
app.mainloop()
