# Exercise 61 - Checking for values
# Write a program that generates a list with contents of your choice
list_1 = list(range(31))

#Now let the user input at least three different things
print ("Give me three numbers that i can lookup in my list.")
no_1 = int(input())
no_2 = int(input())
no_3 = int(input())

#Check whether these inputs are part of your list or not
#Print out an appropriate answer
if no_1 in list_1:
    print (f"Number {no_1} is in the list! Congratulations!")
else:
    print (f"No hit for number {no_1}.")

if no_2 in list_1:
    print (f"Number {no_2} is in the list! Congratulations!")
else:
    print (f"No hit for number {no_2}.")

if no_3 not in list_1:
    print (f"No hit for number {no_3}.")
else:
    print (f"Number {no_3} is in the list! Congratulations!")
