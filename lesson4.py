#Create a list
from itertools import count
from tkinter.font import names

names = ["Blerta","Erosi","Blinera","Ylli"]

#Iterat in the names list and print every name
for name in names:
    print(name)

#############################

sentence = "Hello World"

for character in sentence:
    if character.isalpha(): # Check the character
        print(character)



# Range Function

for number in range(1,6): #prints number from the number 1 to 5 more intail n to n-1
    print(number)

############################

numbers = [12,45,75,34,8,98,14,99,34]

#Intilaze a varable "maximum" with the first value from the list "numbers"

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
        print("The maximum value in the list is:", maximum)




count = 1

while count <= 5:
     print("Iteration", count)
     count += 1



#infinite loop

while True:
    user_input = input("Enter a positive number: ")


    #Check if the input is numeric
    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break


            print("invalid input please try again")

            print("You have entered a vlaid positive number:", number)




