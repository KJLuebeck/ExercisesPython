# Exercise 12 - Slicing of lists
#generate two different lists with contents of your choice
list_1 = list(range(20))
list_2 = list(range(3,30))

# Let the user input four numbers
no_1 = int(input("Please give me a number!"))
no_2 = int(input("Please give me a second number!"))
no_3 = int(input("Please give me a third number!"))
no_4 = int(input("One last number please!"))

# If the numbers entered are bigger than the length of the lists
# ask a second time for smaller numbers

if len(list_1) > no_1 and len(list_1) > no_2 and len(list_2) > no_3 and len(list_2) > no_4:
    print (list_1[no_1:no_2])
    print (list_2[no_3:no_4])
else:
    print ("The numbers are to big! I need smaller numbers.")

    no_1 = int(input("Please give me a smaller number!"))
    no_2 = int(input("Please give me a second number!"))
    no_3 = int(input("Please give me a third number!"))
    no_4 = int(input("One last number please!"))

    if len(list_1) > no_1 and len(list_1) > no_2 and len(list_2) > no_3 and len(list_2) > no_4:
        print (list_1[no_1:no_2])
        print (list_2[no_3:no_4])

# If numbers are still to big, slice until the last number
    else:
        print (list_1[no_1::])
        print (list_2[no_3::])
