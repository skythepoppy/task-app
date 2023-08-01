from modules import functions
import PySimpleGUI as sg # import this specific gui library/package as "sg"
import time

sg.theme("LightGreen2")  # sets the theme of the window

# Below are the features of the window
clock = sg.Text("", key="clock", font=("Courier New",15))
label = sg.Text("Type in a task")   # label using .text
input_box = sg.InputText(tooltip="Enter a task", key="todo")
add_button = sg.Button("Add",tooltip = "Add a task", size = 15, font=("Courier New",20,"bold"))   # adds the "Add" button
list_length = sg.Text("", key="length")
length_message = sg.Text("Number of Tasks to complete: " )
list_box = sg.Listbox(values=functions.get_todos(),     # values expects a list
                      key="todos",
                      enable_events=True,   # expects a boolean value
                      size=[45, 10])     # size of the list box
edit_button = sg.Button("Edit", tooltip = "Edit a task")     # adds the "Edit" button
complete_button = sg.Button("Complete", tooltip = "Complete a task")     # adds the "Complete" button
exit_button = sg.Button("Exit",size = 15, font=("Courier New",20,"bold"))     # adds the "Exit" button

# Below is the initialization of the Window and formats it with lists of PySimpleGui objects via layout
window = sg.Window('My To-Do List App',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [length_message,list_length],
                           [exit_button]], # title of the window with a specific format via layout
                   font=('Courier New', 20))    # font(str(font name),font size)
while True:
    event, values = window.read(timeout=200)     # displays window onto the screen
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # displays number of tasks to do upon opening window
    task_length = functions.get_todos()
    window["length"].update(len(task_length))

    match event:
        case "Add":

            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)     # updates the list box with new added todo/task
            window['todo'].update(value='')  # updates the input box
            window["length"].update(len(task_length))   # updates number of tasks to do

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)    # updates the list box with new edited todos/task
                window['todo'].update(value='')  # updates the input box
                window["length"].update(len(task_length))   # updates number of tasks to do
            except IndexError:
                sg.popup("Please enter an item to edit!", font=("Arial",20))   # popup creates a popup window
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)     # removes the specified value in todo_to_complete
                functions.write_todos(todos)

                window['todos'].update(values=todos)    # updates the list box (completes/deletes that item)
                window['todo'].update(value='')     # updates the input box
                window["length"].update(len(task_length))   # updates number of tasks to do
            except IndexError:
                sg.popup("Please enter an item to complete!", font=("Arial",20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:     # WIN_CLOSED closes window
            break
window.close()     # closes the window