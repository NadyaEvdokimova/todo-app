from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"Today is {now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + '\n'
        todos = get_todos()
        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, todo in enumerate(todos):
            print(f"{index + 1}. {todo.strip("\n")}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = get_todos()
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number -= 1
            todos = get_todos()
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with this number.")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue
    elif "exit" in user_action:
        break
    else:
        print("Hey, you entered an unknown command")

print("Bye")





