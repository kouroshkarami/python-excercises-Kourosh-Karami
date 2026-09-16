'''
L4

Q1. Login




correct_username = "admin"

correct_password = "1234"


username = input("Enter your username")

password = input("Enter your password")

if username != correct_username or password != correct_password:
    print("Wrong username or password please try again")
    
else:
    print("welcome")




Q2.Discount




price = int(input("Enter product price"))

if price >= 10**6:
    print("Final price(20% Discount applied):", price * 0.8)

elif price >= 500000:
    print("Final price(15% Discount applied):", price * 0.85)
    
elif price < 500000:
    print("Final price(10% Discount applied):", price * 0.9)



Q3.Check mouse





products = ["laptop","mouse","keyboard","monitor"]

select = input("Enter desired product")

if select not in products:
    print("This product is unavailable")
else:
    print("This product is available")





Q4. Speed check




speed = int(input("What was their speed"))

if speed > 120:
    print("Dangerous speed")
    
elif speed >= 80:
    print("High speed")

elif speed < 80:
    print("Normal speed")


Q5.Odd numbers



numbers = []

for i in range(15,116):
    if i % 2 == 1:
        numbers.append(i)
    


Q6.Calculation of diffrent name lengths





names = ["ali","sara","sarina","shayan"]


count = 0

for i in names:
    print(len(i))
    
    count = count = len(i)




Q7.Calculation of squared numbers



numbers = [1, 7, 15, 23, 31, 44]


new_list = []


for i in numbers:
    new_list.append(i**2)
    




Q8.Short names



users = ["ali","vahid","mohammadreza","hamidreza","gholamreza","amir","sara","maryam"]

count = 0



for i in users:
    if len(i) < 5:
        print(i)
        count = count + 1
        print(count)




Q9.Price inflation



old_prices = [750,350,500,850,1200]

new_prices = []

for i in old_prices:
    new_prices.append(i * 1.1)



Q10.Celsius--->Fahrenheit






celsius_list = [32.5,45,28.5,20]

fahrenheit_list = []

for i in celsius_list:
    fahrenheit_list.append(i *1.8 +32)



Q11.Calculating product profit



buy_prices = [100,200,150,400]

sell_prices = [130,250,190,500]

profits = []


for i in range(0,4):
    profits.append(sell_prices[i] - buy_prices[i])
    


Q12.Shopping cart



cart = []

for i in range(5):
    product=input("Enter the desired product")
    if len(product) <6:
        cart.append(product)
'''























































































































































































































































































































































































































