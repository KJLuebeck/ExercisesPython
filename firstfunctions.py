#Exercise 28 - Your first functions
#create a program that defines functions for the four mathematical basic operations (+,-,* and/)
def sum (a, b):
    result_sum = a+b
    return result_sum

def sub (a, b):
    result_sub = a-b
    return result_sub


def multi (a, b):
    result_multi = a*b
    return result_multi

def div (a, b):
    result_div = a/b
    return result_div

no_1 = int(input("Give me three numbers:\n"))
no_2 = int(input())
no_3 = int(input())

sum_1 = sum(no_1, no_2)
print (f"{no_1}+{no_2}={sum_1}")
sum_2 = sum(no_2, no_3)
print (f"{no_2}+{no_3}={sum_2}")
sum_3 = sum(no_1, no_3)
print (f"{no_1}+{no_3}={sum_3}")


sub_1 = sub(no_1,no_2)
print (f"{no_1}-{no_2}={sub_1}")
sub_2 = sub(no_2, no_3)
print (f"{no_2}-{no_3}={sub_2}")
sub_3 = sub(no_1, no_3)
print (f"{no_1}-{no_3}={sub_3}")

multi_1 = multi(no_1,no_2)
print (f"{no_1}*{no_2}={multi_1}")
multi_2 = multi(no_2, no_3)
print (f"{no_2}*{no_3}={multi_2}")
multi_3 = multi(no_1, no_3)
print (f"{no_1}*{no_3}={multi_3}")

div_1 = div(no_1,no_2)
print (f"{no_1}/{no_2}={div_1}")
div_2 = div(no_2, no_3)
print (f"{no_2}/{no_3}={div_2}")
div_3 = div(no_1, no_3)
print (f"{no_1}/{no_3}={div_3}")

print ( (div(no_1,no_2))+ (multi(no_1, no_3)) )
