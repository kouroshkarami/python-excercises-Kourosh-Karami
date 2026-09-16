'''
L5


Q1.Grading system


scores = [20,17,9,13,7,20,18,3,1,14]

passed = 0

failed = 0


for i in scores:
    if i <10:
        print("Failed")
    else:
        print("Passed")


Q2.Showcasing passed students




students = ["ali","vahid","sara","hamid","reza","elham","mohsen","zahra","paniz","parmida"]

scores = [20,17,9,13,7,20,18,3,1,14]

for i in range(0,10):
    if scores[i] >= 10:
        print(students[i])
        


Q3.Product list




product_list = []

while True:
    selection = input("Enter desired product")
    if selection == "exit":
        break
    else:
        product_list.append(selection) 
        




Q4.ATM system





while True:
    print("Menu:")
    print("1. Balance")
    print("2. Transfer")
    print("3. Deposit")
    print("4. Other")
    print("5. Exit")
    selection = input("Select your action:")
    if selection == "1":
        print("Balance has been selected")
    elif selection == "2":
        print("Transfer has been selected")
    elif selection == "3":
        print("Deposit has been selected")
    elif selection == "4":
        print("Other options selected")
    elif selection == "5":
        again = input("Would you like to do any other actions or exit?")
        print("Goodbye")
        break
            

Q5.Login system

CorrectUsername = "admin"

CorrectPassword = "1234"




while True:
    Username = input("Enter your username")
    Password = input("Enter your password")
    if Username != CorrectUsername or Password != CorrectPassword:
        print("Incorrect username or password")
    else:
        print("Access granted")
        break

Q6.Login system with limited tries:
    


CorrectUsername = "admin"

CorrectPassword = "1234"



for i in range(3):
    Username = input("Enter your username")
    
    Password = input("Enter your password")
    if Username == CorrectUsername and Password == CorrectPassword:
        print("Access granted")
        break
    else:
        print("Incorrect username or password please try again")
else:
    print("You are blocked")
     


Q7.Restaurant ordering system:
    

print("Welcome to our restaurant! our menu includes:")
print("burger, pizza, pasta, chicken breast and potatoes")

receipt = []

foods = ["burger","pizza","pasta","chicken breast","potatoes"]

while True:
        order = input("Which meal do you want to order?")
        if order in foods:
            receipt.append(order)
            print("Selected meal is available order has been submitted")
        
        elif order == "order":
            print("Orders have been submitted")
            break 
for i in receipt:
        print (i)




Q8.Simple chatbot



print("Hello")
while True:
    user = input("")
    if user == "bye":
        print("bye")
        break
    else:
        print("Chatbot's response")

'''






















        
    
    




























        





























































































































