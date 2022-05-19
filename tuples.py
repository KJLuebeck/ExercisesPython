# Evercise 20 - Working with tuples

#Write a program that creates four tuples of different length
#length should be dictated by user
#print out
print ("Give me three different numbers for my tuples:")
no_1 = int(input())
no_2 = int(input())
no_3 = int(input())

tuple_1 = tuple(range(no_1))
tuple_2 = tuple(range(no_2))
tuple_3 = tuple(range(no_3))
print (f"This is tuple_1:\n{tuple_1}")
print (f"This is tuple_2:\n{tuple_2}")
print (f"This is tuple_3:\n{tuple_3}")
print (type(tuple_1))
# user chose one entry from each tuple to be displayed
print ("Choose one entry from each tuple to be displayed:")
entry_1 = int(input())
entry_2 = int(input())
entry_3 = int(input())
print (f"This is the entry from tuple_1:{tuple_1[entry_1]}")
print (f"This is the entry from tuple_2:{tuple_2[entry_2]}")
print (f"This is the entry from tuple_3:{tuple_3[entry_3]}")
# Try to generate a tuple with duplicate values
tuple_4 = (1,)*2+(2,)*2
print (tuple_4)
