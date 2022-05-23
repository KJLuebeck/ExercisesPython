number = int(input("Please type in a number: ")) #typed in 5
while number !=8: # --> True 5 not equal 8
    print ("Wrong choice")
    number = int(input("Try again: "))

#while-loop 2

sum1 = 1
while sum1 < 1000:
    sum1 += sum1
    print(sum1)

#dieses programm als while und for schleife alternativ
list1 = list(range(101))
random.shuffle(list1)

i=0
while list1[i] !=50:
    print (f"We are in iteration {i+1} and 50 wasnt found yet")
    i+=1
#for loops

for elem in list1:
    if elem!=50:
        print ("we didnt find the fifty yet")
    else:
        break
