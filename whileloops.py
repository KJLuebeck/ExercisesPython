#Exercise 24 - 3 while loops
#Write a program that uses while loops to finish the tasks below
#1: Searching for a specific number in an integer list of unknown length
list_1 = [5,23,57,12,7,45,1,9,5,7,44,2,99,3,7,22,13,6,8,67,44]
no_1 =int(input("What number are you looking for?\n"))

i=0
while list_1[i] !=no_1:
    print("No hit!")
    i+= 1
print (f"You found the {no_1} after {i} iterations.")

#2: Multiplying all elements with each other of an integer list of unknown length
i=0
result =1
while i < len(list_1):
    result = result * list_1[i]
    i += 1
print (f"The result is {result}")

#3: Printing out the contents of a string list of unknown length elementwise

i=0
while i < len(list_1):
    print(f"Zahl {i} ist: {list_1[i]}")
    i+= 1
