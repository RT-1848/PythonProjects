# an empty list to store tasks
tasks = []


# Function to display the current list
def show_tasks():
  index = 1
  if tasks:
    print("Your to-do list:")
    for task in tasks:
      print(index, " ", task)
      index += 1
  elif not tasks:
    print("Your to-do list is empty.")


# Function to add a task to list
def add_task():
  task = input("Enter the task to add: ")
  tasks.append(task)
  print('Task', task, "added to your to-do list.")


# Function to remove a task from list
def remove_task():
  show_tasks()
  if tasks:
    try:
      task_number = int(input("Enter the task number to remove: ")) - 1
      if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print('Task', removed_task, "has been removed from your to-do list.")
      else:
        print("Invalid task number. Please enter a valid task number.")
    except ValueError:
      print("Invalid input. Please enter a valid task number.")


# Main loop for the list program
while True:
  print("\nOptions:")
  print("1. Show to-do list")
  print("2. Add a task")
  print("3. Remove a task")
  print("4. Quit")

  choice = input("Enter your choice: ")

  if choice == "1":
    show_tasks()
  elif choice == "2":
    add_task()
  elif choice == "3":
    remove_task()
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please enter a valid option.")
