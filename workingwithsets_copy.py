#Exercise 21 - Working with sets
#Write a program that creates four sets of different lengths
#length should be deictated by user

print ("Give me four different numbers for my sets:")
no_1 = int(input())
no_2 = int(input())
no_3 = int(input())
no_4 = int(input())

print ("Give me four names for my new set:")
name_1 = input()
name_2 = input()
name_3 = input()
name_4 = input()

set_1 = set(range(no_1))
set_2 = set(range(no_2))
set_3 = set(range(no_3))
set_4 = set(range(no_4))
print (type(set_1))
set_5 = {name_1, name_2, name_3, name_4}
print (type(set_5))

#Print out the sets
print (f"This is set_1:\n{set_1}")
print (f"This is set_2:\n{set_2}")
print (f"This is set_3:\n{set_3}")
print (f"This is set_4:\n{set_4}")
print (f"This is set_4:\n{set_5}")
