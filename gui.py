from modules import functions
import PySimpleGUI as sg # import this specific gui library/package as "sg"

# Below are the features of the window
label = sg.Text("Type in a task")   # label using .text
input_box = sg.InputText(tooltip = "Enter a task")  # input box with tooltip
add_button = sg.Button("Add")   # adds a button


# Below is the initialization of the Window and formats it with lists of PySimpleGui objects via layout
window = sg.Window('My To-Do List App',
                   layout = [[label],[input_box,add_button]])    # title of the window with a specific format via layout
window.read()     # displays window onto the screen
window.close()     # closes the window