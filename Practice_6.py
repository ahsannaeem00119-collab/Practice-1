#Calculator using try/except features
import math
while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. view history")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3", "4" , "5" , "6" , "7" , "8"]:
        try:
            
            if choice == "1":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
                
                with open("history.txt", "a") as file:
                    file.write(f"{num1} + {num2} = {result}\n")

            elif choice == "2":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
                
                with open("history.txt", "a") as file:
                    file.write(f"{num1} - {num2} = {result}\n")

            elif choice == "3":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: ")) 
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
                
                with open("history.txt", "a") as file:
                    file.write(f"{num1} * {num2} = {result}\n")

            elif choice == "4":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
                
                with open("history.txt", "a") as file:
                    file.write(f"{num1} / {num2} = {result}\n")
            
            elif choice == "5":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result= num1**num2
                print(f"The result of {num1} ** {num2} is: {result}")
                
                with open("history.txt", "a") as file:
                    file.write(f"{num1} ** {num2} = {result}\n")
                
            elif choice == "6":
                num=float(input("Enter a number: "))
                result=math.sqrt(num)
                print(f"The square root of {num} is: {result}")
                
                with open("history.txt", "a") as file:
                    file.write(f"sqrt({num}) = {result}\n")

            elif choice == "7":
                try:
                    with open("history.txt" , "r") as file:
                        print("-----History-----")
                        print(file.read())
                except FileNotFoundError:
                    print("No history found. Please perform some calculations first.")
            elif choice == "8":
             print("Goodbye!")
             break   
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError as e:
            print(e)

    

    else:
        print("Invalid choice. Please try again.")