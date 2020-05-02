import sys, os
sys.path.append(os.path.abspath('./'))
from NeuronNetwork import *
from tkinter import *

class App(object):
    
    def __init__(self):
        self.root = Tk()

        WIDTH = 600
        HEIGHT = 400

        self.Canva = Canvas(self.root, width = WIDTH, height = HEIGHT)
        self.Canva.create_rectangle(0, 0, WIDTH, HEIGHT, fill = '#7f7f7f')
        CIRCLE_WIDTH = (WIDTH - 30)/2
        self.circle_black = self.Canva.create_oval(10, (HEIGHT - CIRCLE_WIDTH)/2, CIRCLE_WIDTH, CIRCLE_WIDTH + (HEIGHT - CIRCLE_WIDTH)/2, fill = 'green', outline = '')
        self.circle_white = self.Canva.create_oval(20 + CIRCLE_WIDTH, (HEIGHT - CIRCLE_WIDTH)/2, 20 + 2*CIRCLE_WIDTH, CIRCLE_WIDTH + (HEIGHT - CIRCLE_WIDTH)/2, fill = 'green', outline = '')
        self.Canva.pack()

        self.root.mainloop()

App()