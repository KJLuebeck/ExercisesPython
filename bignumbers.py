# Big numbers
print ("Hey, give me two numbers!")
no_1 = float(input())
no_2 = float(input())
if (no_1 + no_2) > 100:
    print ("That is a big number.")

elif (no_1 + no_2) > 10:
    print ("That is a mediocre number.")

elif (no_1 + no_2) > 5:
    print ("That is a small number.")

else:
    print ("This is a very small number.")
