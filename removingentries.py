# Exercise 14 - Removing entries
# Write a program that generates at least three different lists
list_1 = list(range(15))
list_2 = list(range(11))
list_3 = list (range(3,30))
#Print these lists out
print (f"This ist list 1:\n{list_1}")
print (f"This ist list 2:\n{list_2}")
print (f"This ist list 3:\n{list_3}")
#Ask the user for one entry from each list he wants to have removed
entry_1 = int(input("Which number do you want to remove from list 1?\n"))
entry_2 = int(input("Which number do you want to remove from list 2?\n"))
entry_3 = int(input("Which number do you want to remove from list 3?\n"))
#let the program remove the entry
list_1.remove(entry_1)
list_2.remove(entry_2)
list_3.remove(entry_3)
#Print out the new lists
print (f"This is the new list 1 missing number {entry_1}:\n{list_1}")
print (f"This is the new list 2 missing number {entry_2}:\n{list_2}")
print (f"This is the new list 3 missing number {entry_3}:\n{list_3}")
