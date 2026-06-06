# Simple note-taking application
while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Clear notes")
    print("4. Count notes")
    print("5. Search notes")
    print("6. Exit")

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
        with open("notes.txt", "w") as file:
            pass  # Clear the notes file
        print("All notes cleared successfully!")
    
    elif choice == "4":
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            print(len(notes))
            
        
    
    elif choice == "5":
        print("Search a note by a keyword:")
        keyword = input("Enter keyword: ")
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            found_notes = [note for note in notes if keyword in note]
            if found_notes:
                print("\nFound notes:")
                for idx, note in enumerate(found_notes, 1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found containing the keyword.")

    elif choice == "6":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        