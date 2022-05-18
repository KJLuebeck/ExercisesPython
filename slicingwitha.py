# Slicing with a
# Write a program that generates a list with the help of the range function
length = int(input("How long should your list be?"))
list_1 = list(range(length))
print (list_1)
# User should input length of the list and four different numbers for Slicing
# first number: endpoint of new lists
no_1 = int(input("Give me the endpoint for slicing your list."))
# second number: starting point
no_2 = int(input("Give me the starting point for your list."))
# numbers three and four: skips you can do with Slicing
print ("Give me two points for skips in the list.")
no_3 = int(input())
no_4 = int(input())
# print out new lists
list_2 = list_1[:no_1] # Anfang Liste - Endpunkt no_1
print (f"Your list with the endpoint {no_1}:")
print (list_2)
list_3 = list_1[no_2::] # Startpunkt no_2 bis Ende Liste
print (f"Your list with the starting point {no_2}:")
print (list_3)
list_4 = list_1[::no_3] # komplette Liste, aber Zahlen werden je nach Eingabe von no_3 übersprungen
print (f"Your list with skips every {no_3} numbers:")
print (list_4)
list_5 = list_1[::no_4] # wie bei no_3
print (f"Your list with skips every {no_4} numbers:")
print (list_5)
