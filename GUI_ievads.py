# PySimpleGUI kalkulators
from cmath import *
import PySimpleGUI as sg

layout = [
    [sg.Text('Produkts:', size = (16,1)),sg.Input(k='-IN-'),sg.Button('=')],
    [sg.Text('Rezultāts: ', size = (16,1)), sg.Input(k='-OUT-')] 
]
window = sg.Window('kalkulators', layout)
while True:
    event, values = window.read()
 # print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "=" :
        window['-OUT-'].update(eval(values['-IN-']))
window.close()
