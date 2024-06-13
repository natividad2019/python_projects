'''
for loop 
for item in list_of_items:
  #Do something to each item 
  print(item) will goes next line
'''

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#   print(fruit)
#   print(fruit + "pie")
# print(fruits)


# For loop with range
# for number in range (1, 11, 3)
#   print(number)

# for number in rang(a, b):
#   print(number)

# for number in range(1,11, 3):
# #   print(number)

# total = 0 
# for number in range(1, 101): # number = 1 
#   print(number)
#   #total += number
#   total = total + number 
#   # total = 0  + 1 = 1
#   #total = 1 + 2 = 3
#   #total = 3 + 3 = 6
#   #total = 6 + 4 = 10
#   #total = 10 + 5 = 15
#   #total = 15 + 6 = 21
#   #total = 21 + 7 = 28 
#   #total = 28 + 8 = 36
#   #total = 36 + 9 = 45
#   #total = 45 + 10 = 55
#     #print(total)

# print(total)


# you are going to write a program that automatically prints the solution to the FizzBuzz game.  These are the rules of the FizzBuuzz game.
# your program should print each number from 1 to 100 in turn and include the number 100
# when the number is divisible by 3,  then instaed of printing the number it should print "Fizz"
# when the number is divisible by 5,  then instaed of printing the number it should print "Buzz"
# when the number is divisible by 3 and 5,  then instaed of printing the number it should print "FizzBuzz"

target = 100
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)