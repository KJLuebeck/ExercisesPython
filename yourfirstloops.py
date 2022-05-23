#Exercise 23 - Your first loops
#Write one loop that sums up all numbers in the setted range print result

#Summe1 = 0
#For i = 0-20:
#   Summe1 = addition 1 to i
#print sum of all additions


sum_1 = 0
for i in range(21):
    sum_1 += i
print(sum_1)

#Write a loop thats sums up only the even numbers in the setted range print result
#Summe2 = 0
#For i = 0-20
#   IF i modulo 2 equal 0
#       add i+1 to sum_2
#       print i
#print sum of all even numbers sum_2

sum_2 = 0
for i in range(21):
    if i%2 == 0: #Rest = 0 --> Zahl ist gerade
        sum_2 += i+1
        print(i)
print(sum_2)
#Write a loop that generates a list that contains the values of the range in reverse order

#create empty list_1
#For i = 0-20
#   append i to list_1
#reverse list_1
#print list_1
list_1 = []
for i in range(21):
    list_1.append(i)
list_1.reverse()
print(list_1)
