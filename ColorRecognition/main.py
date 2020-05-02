import sys, os
sys.path.append(os.path.abspath('./'))
from NeuronNetwork.NeuronNetwork import * 
from tkinter import *
from tkinter import messagebox
import random 
import numpy as np
import pickle

class App(object):
    
    def __init__(self):
        self.root = Tk()

        WIDTH = 600
        HEIGHT = 400

        self.Canva = Canvas(self.root, width = WIDTH, height = HEIGHT)
        self.Canva.create_rectangle(0, 0, WIDTH, HEIGHT, fill = '#7f7f7f')
        
        self.current_color = self.random_rgb_color()

        CIRCLE_WIDTH = (WIDTH - 30)/2
        self.circle_black = self.Canva.create_oval(10, (HEIGHT - CIRCLE_WIDTH)/2, CIRCLE_WIDTH, CIRCLE_WIDTH + (HEIGHT - CIRCLE_WIDTH)/2, outline = '')
        self.circle_white = self.Canva.create_oval(20 + CIRCLE_WIDTH, (HEIGHT - CIRCLE_WIDTH)/2, 20 + 2*CIRCLE_WIDTH, CIRCLE_WIDTH + (HEIGHT - CIRCLE_WIDTH)/2, outline = '')

        self.update_color()

        self.Canva.create_text(CIRCLE_WIDTH/2, (HEIGHT - CIRCLE_WIDTH)/2 + CIRCLE_WIDTH/2, text = "TEXT", font = 'Arial 50', fill = 'black')
        self.Canva.create_text(CIRCLE_WIDTH + 20 + CIRCLE_WIDTH/2, (HEIGHT - CIRCLE_WIDTH)/2 + CIRCLE_WIDTH/2, text = "TEXT", font = 'Arial 50', fill = 'white')

        self.Canva.grid(
            row = 0,
            column = 0,
            columnspan = 2
        )

        self.Button_black = Button(self.root, text = 'Black', font = 'Arial 20', command = lambda: self.color_chosen(0))
        self.Button_black.grid(
            row = 1,
            column = 0
        )

        self.Button_white = Button(self.root, text = 'White', font = 'Arial 20', command = lambda: self.color_chosen(1))
        self.Button_white.grid(
            row = 1,
            column = 1
        )

        self.label_prediction_var = StringVar()
        self.Label_prediction = Label(self.root, textvariable = self.label_prediction_var, font = 'Arial 20')
        self.Label_prediction.grid(
            row = 2,
            column = 0,
            columnspan = 2
        )

        self.AI = None
        self.file_training = open('ColorRecognition/training_datas', 'a')

        try:
            file = open('ColorRecognition/AI_datas', 'rb')
            self.AI = pickle.load(file, encoding = 'bytes')
        
        except:
            self.AI = NeuronNetwork(3, 1, 1, np.array([3]))

        self.run_ai()

        def on_closing():
            ask = messagebox.askquestion(title='Exit', message='Do you want to save the training session ?')
            
            if ask == 'yes':
                file = open('ColorRecognition/AI_datas', 'wb')
                self.AI = pickle.dump(self.AI, file)
            
            self.root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', on_closing)
        self.root.mainloop()

    def random_rgb_color(self):
        r = random.randrange(0, 255, 1)
        g = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)

        return[r,g,b]

    def update_color(self):
        color_hex = '#'
        for i in range(0,3):
            a = hex(self.current_color[i])[2:]
            if len(a) == 1:
                color_hex += '0'

            color_hex += a 

        self.Canva.itemconfig(self.circle_black, fill=color_hex)
        self.Canva.itemconfig(self.circle_white, fill=color_hex)

    def color_chosen(self, color):
        training_input = np.array([
            [self.current_color[0]],
            [self.current_color[1]],
            [self.current_color[2]]
        ])

        line = ''
        for i in range(3):
            line += str(self.current_color[i])
            line += ','

        line += str(color)
        line += '\n'

        self.file_training.write(line)

        training_output = np.array([color])

        self.AI.train(training_input, training_output)

        self.current_color = self.random_rgb_color()
        self.update_color()

        self.run_ai()

    def run_ai(self):
        input = np.array([
            [self.current_color[0]],
            [self.current_color[1]],
            [self.current_color[2]]
        ])

        result = np.around(self.AI.compute(input), decimals = 2)[0,0]

        if result > 0.5:
            self.label_prediction_var.set('White : ' + str(result))
        else:
            self.label_prediction_var.set('Black : ' + str(result))

App()