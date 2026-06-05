#user login system
users = {}
while True:
    print("1. Register")
    print("2. Login")
    print("3. Reset Password")
    print("4. View Registered Users")
    print("5. Total Users")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    #Registration
    if choice == '1':
        username =input("Enter username: ")
        password = input("Enter password: ")
        if username in users:
            print("Username already exists. Please choose a different username.")
        else:
            print("Confirm password: ")
            confirm_password = input()
            if password == confirm_password:
                users[username] = password
                print("Registration successful!")
            else:
                print("Passwords do not match. Please try again.")
    #Login
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in users and users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    
    #Reset password      
    elif choice == '3':
        username = input("Enter username: ")
        
        if username in users:
            new_password = input("Enter new password: ")
            users[username] = new_password
            print("Password reset successful!")
        else:
            print("Username not found. Please register first.")
        
    elif choice == '4':
        for username in users:
          print("Registered user:", username)
          
    elif choice == '5':
        print("Total count of registered users:", len(users))
        
        
    #Exit the program  
    elif choice == '6':
        print("Exiting the program.")

        break

    


