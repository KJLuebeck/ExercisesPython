#Exercise 6 - Comparing numbers
print ("Hey, give me four numbers!")
no_1 = float(input())
no_2 = float(input())
no_3 = float(input())
no_4 = float(input())

if no_1 == no_2 and no_3 == no_4:
    print ("Hey, how funny, do you have no ideas?")

elif no_1 == no_3 and no_2 == no_4:
    print ("Boring!")

elif no_1 == no_4 or no_2 == no_3:
    print ("At least a hit.")

else:
    print ("No match at all.")
