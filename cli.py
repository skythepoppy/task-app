'''from functions import get_todos, write_todos  pulls functions from a separate file
# above, functions is a module
'''

from modules import functions   # from modules folder, use functions module
import time


action_prompt = "Type add, show, edit, complete, length or quit: "
now = time.strftime("%b %d, %Y %H:%M:%S")
print("The current time stamp is: ", now)


while True:

    user_action = input(action_prompt)
    user_action = user_action.strip()   #   strips trailing spaces



    if user_action.startswith("add"):
        todo = user_action[4:]

        # function to return list
        todos = functions.get_todos()

        todos.append(todo +'\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):    # | represents a bitwise Or operator

        todos = functions.get_todos()

        # new_todos= [item.strip('\n') for item in todos]     #strips the \n (list comprehension)

        for index, item in enumerate(todos):    #stores item and then pairs it with it's index
            item = item.strip('\n')     #(list comprehension to strip)
            output = f"{index + 1} - {item}"    #uses fstring to format the output
            print(output)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new task: ")
            todos[number] = new_todo + '\n'

            # adds new item into todos list in todos.txt
            functions.write_todos(todos)
        except ValueError:  # provides an alternative based on error
            print("Your command is not valid")
            continue    # runs another cycle of the while loop

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            # below identifies which task to remove and removes it (using pop())
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # below implements the todos.pop into the todos.txt file (removes an item)
            functions.write_todos(todos)

            complete_message = f"The task ({task_to_remove}) is completed and removed from the list."
            print(complete_message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("length"):
        print("Number of tasks in list: ", len(todos))   #uses len() to find length

    elif user_action.startswith("quit"):
        break

    else:
        print("Command is not valid, please try again")

print("Goodbye!")







