from modules import functions
import PySimpleGUI as sg # import this specific gui library/package as "sg"

# Below are the features of the window
label = sg.Text("Type in a task")   # label using .text
input_box = sg.InputText(tooltip="Enter a task", key="todo")  # input box with tooltip & key
add_button = sg.Button("Add")   # adds a button


# Below is the initialization of the Window and formats it with lists of PySimpleGui objects via layout
window = sg.Window('My To-Do List App',
                   layout=[[label],[input_box,add_button]],  # title of the window with a specific format via layout
                   font=('Arial', 20))    # font(str(font name),font size)
while True:
    event, values = window.read()     # displays window onto the screen
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:     # WIN_CLOSED closes window
            break
window.close()     # closes the window