# Simple note-taking application
while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        with open("notes.txt", "a") as file:
            note = input("Enter your note: ")
            file.write(note + "\n")
            print("Note added successfully!")
    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\nYour notes:")
                print(file.read())
                
        except FileNotFoundError:
            print("No notes found. Please add a note first.")
            
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        
    