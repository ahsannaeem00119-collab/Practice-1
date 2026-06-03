#making a pragram which will ask the user to enter their name,subject marks  and then calculate their average marks 

name=input("Enter your name: ")
marks1=int(input("Math: "))
marks2=int(input("English: "))
marks3=int(input("Science: "))
marks4=int(input("Social Studies: "))
marks5=int(input("physics: "))

average=(marks1+marks2+marks3+marks4+marks5)/5


grade=""
if average>=90:
    grade="A*"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
else:
    grade="F"
    
print("Name :", name)  
print("Average Marks :", average)
print("Grade :", grade)  

print(f"{name}, your average marks are {average} and your grade is {grade}.")