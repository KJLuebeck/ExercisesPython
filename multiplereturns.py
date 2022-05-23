#Exercise 31 - multiple returns
#In exercise 28 (firstfunctions) you created four different functions
#now combine them into a nex function that returns all four results at once
def mathoperations (a, b):
    result_sum = a+b
    result_sub = a-b
    result_multi = a*b
    result_div = a/b
    return result_sum, result_sub, result_multi, result_div

no_1 = int(input("Give me three numbers:\n"))
no_2 = int(input())
no_3 = int(input())

sum_1,sub_1, multi_1, div_1  = mathoperations(no_1, no_2)
print (f"{no_1}+{no_2}={sum_1}")
print (f"{no_1}-{no_2}={sub_1}")
print (f"{no_1}*{no_2}={multi_1}")
print (f"{no_1}/{no_2}={div_1}")

sum_2,sub_2, multi_2, div_2 = mathoperations(no_2, no_3)
print (f"{no_2}+{no_3}={sum_2}")
print (f"{no_2}-{no_3}={sub_2}")
print (f"{no_2}*{no_3}={multi_2}")
print (f"{no_2}/{no_3}={div_2}")

sum_3, sub_3, multi_3, div_3 = mathoperations(no_1, no_3)
print (f"{no_1}+{no_3}={sum_3}")
print (f"{no_1}-{no_3}={sub_3}")
print (f"{no_1}*{no_3}={multi_3}")
print (f"{no_1}/{no_3}={div_3}")
