'''
q3.1. checks if the number is positive, negative or zero:



number = int(input('enter number here'))

if number == 0:
    print("your number is zero")
elif number < 0:
    print("your number is  negative")
else:
    print("your number is positive")



q3.2.checks if the numbers are even or odd


number = int(input("enter number here"))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


q3.3.calculator:
    


Numb_1 = int(input("enter first number"))

operation = input("enter operation")


Numb_2 = int(input("enter second number"))



if operation == "+":
    print(Numb_1 + Numb_2)
elif operation == "-":
    print(Numb_1 - Numb_2) 
elif operation == "/":
    print(Numb_1 / Numb_2)
elif operation == "*":
    print(Numb_1 * Numb_2)
elif operation == "**":
    print(Numb_1 ** Numb_2)
else:
    print("Error")
    
    
    
    
3.4.Grading system for college: if 18-20 --> A
                               if 15-17 --> B
                               if 10-14 --> C
                               if 0-10 --> f (fail)
                              



grade = float(input("Enter grade"))

if grade < 0  or grade > 20:
    print=("Invalid Grade")
elif grade >= 18:
    print("A") 
elif grade >= 15:
    print("B")
elif grade >= 10:
    print("C")
else:
    print("F") 
    


q3.5.online shop with discount code function:
    
    
product = []

price = []


name = input("Enter product name here")




price = int(input("Enter product price here"))





discount_code = input("Enter discount code")


if discount_code == "z14":
    price = price * 0.8
    print("discount applied successfully")
    print("Final price:",price)
else:
    print("Code is incorrect")
    print("You are blocked.")

    

'''






























