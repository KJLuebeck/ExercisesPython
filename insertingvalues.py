#Exercise 62 - Inserting values
#Write a program that generates three lists of different sizes and print them out
list_1 = list(range(31))
print (f"This ist list 1:{list_1}")
list_2 = list(range(2,45))
print (f"This ist list 2:{list_2}")
list_3 = list(range(2,30,2))
print (f"This ist list 3:{list_3}")

#Let the user choose where on these lists he wants to insert which numbers
#Dont forget to check whether the chosen index is part of the list or not

no_1 = int(input("Which number do you want to insert in list 1?\n"))
no_2 = int(input("Where do you want to insert the number?\n"))

if len(list_1) >= no_2:
    list_1.insert(no_2,no_1)
    print (list_1)
else:
    print ("Fail, index outside list.")


no_3 = int(input("Which number do you want to insert in list 2?\n"))
no_4 = int(input("Where do you want to insert the number?\n"))

if len(list_2) >= no_4:
    list_2.insert(no_4,no_3)
    print (list_2)
else:
    print ("Fail, index outside list.")

no_5 = int(input("Which number do you want to insert in list 3?\n"))
no_6 = int(input("Where do you want to insert the number?\n"))

if len(list_3) >= no_6:
    list_3.insert(no_6,no_5)
    print (list_3)
else:
    print ("Fail, index outside list.")
