'''
online#3


number = int(input("Enter number"))

for i in range(1,11):
    print(number*i) 



for i in range(1,11):

    for j in range(1,11):
        print(i,"*", j,"*", i * j)

count = 0
for i in range(0,101,2):
    count +=1
    print(i)
    print(count)


word = input("Enter word")

for i in range(len(word)):
    print(i)



word = input("Enter word")

for i in range(len(word)):
    print(i,word[i])
  

sentence = input("Enter a sentence")
word = input("Enter word")
count = 0
for i in sentence:
    if word == i:
        count+=1
        print("count=",count)



numbers = [10,30,20,45,70,90]

highest = numbers[0]

for i in numbers:
    if i > highest:
        highest = i
        print(highest)



word = input("Enter a word you want backwards")
o = ""

for char in word:
    o= char + o
    print(o)

'''


correct_password = "admin"

password = input("Enter your password")

for i in range(5):
    if password != correct_password:
        print("wrong password please try again")
        password = input("Enter your password")
    elif password == correct_password:
        print("password is correct")
        break
    print("You are blocked from this website")

















































































































































