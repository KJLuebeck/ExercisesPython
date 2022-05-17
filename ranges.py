#Working with range and len
no_1 = int(input("Which length should your list number one have?"))
no_2 = int(input("Which length should your list number two have?"))
no_3 = int(input("Which length should your list number three have?"))
no_4 = int(input("Which length should your list number four have?"))
no_5 = int(input("Where do you want your list to start(number)?"))
no_6 = int(input("Where do you want your list to end(number)?"))

list_1 = list(range(no_1))
print (list_1)
print (f"The length of the list is {(len(list_1))}.")

list_2 = list(range(no_2))
print (list_2)
print (f"The length of the list is {(len(list_2))}.")

list_3 = list(range(no_3))
print (list_3)
print (f"The length of the list is {(len(list_3))}.")

list_4 = list(range(no_4))
print (list_4)
print (f"The length of the list is {(len(list_4))}.")

list_5 = list (range(no_5, no_6+1))
print (list_5)
print (f"The length of the list is {(len(list_5))}.")
