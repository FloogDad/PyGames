import PySimpleGUI as sg
import random

layout = [[sg.Text("What's your question?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Shake the magic 8-Ball!'), sg.Button('Quit')]]

window = sg.Window('Magic 8-Ball',layout)
window.read()