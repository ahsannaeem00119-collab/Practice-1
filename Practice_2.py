# To-do list manager
tasks=[]
while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        try:
            if choice == '1':
                task = input("Enter the task to add: ")
                tasks.append(task)
                print(f'Task "{task}" added to the list.')
                
            elif choice == '2':
                if not tasks:
                    print("No tasks in the list.")
                else:
                    print("To-Do List:")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. {task}")
                        
            elif choice == '3':
                if not tasks:
                    print("No tasks in the list.")
                else:
                    for index,task in enumerate(tasks,start=1):
                        print(f"{index}. {task}")
                        
                        number=int(input("Enter the number of the task to remove: "))
                        tasks.pop(number-1)
                        print("Task removed from the list.")
                        
            elif choice == '4':
                print("Exiting the to-do list manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

    
        
        