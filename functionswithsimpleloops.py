# Exercise 29 - Functions with simple loops
#Write a program that contains two different Functions
#first function should take a list as an argument and return the sum of all elements
#in the list, calculated by a loop

def sum_list (input_list):
    result = 0
    for i in input_list:
        result += i
    return result

list_1 = (range(21))
print (sum_list(list_1))


#second function should take a list and return a list in which the content of the list
#that was used as a parameter are reversed (use a loop as well)

def reverse_list (input_list):
    no_1 = len(input_list)
    input_listreverse = []
    for i in range(no_1): # for i in reverse(range(no_1)) alternativ
        input_listreverse.append(input_list[no_1-i-1])
    return input_listreverse

list_reverse = (reverse_list(list_1))
print(list_reverse)
