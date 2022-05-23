#32 Multiple returns from lists
#Take your functions from exercise 29 and create a new One
#that returns both results at once
#The function should include only one loop
list_1 = (range(21))

def sum_reverse_list (input_list):
    result = 0
    no_1 = len(input_list)
    input_listreverse = []
    for i in range(no_1):
        input_listreverse.append(input_list[no_1-i-1])
        result += (input_list[i]) # input_list[i] Zugriff auf index i in input_list
    return result, input_listreverse

sum, list_reverse = (sum_reverse_list(list_1))
print (sum)
print (list_reverse)
print (sum_reverse_list(list_1))


#def sum_list (input_list):
    #result = 0
    #for i in input_list:
        #result += i
    #return result


#print (sum_list(list_1))


#second function should take a list and return a list in which the content of the list
#that was used as a parameter are reversed (use a loop as well)

#def reverse_list (input_list):
    #no_1 = len(input_list)
    #input_listreverse = []
    #for i in range(no_1): # for i in reverse(range(no_1)) alternativ
    #    input_listreverse.append(input_list[no_1-i-1])
    #return input_listreverse

#list_reverse = (reverse_list(list_1))
#print(list_reverse)
