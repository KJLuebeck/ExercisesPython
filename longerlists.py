# Generate six different lists
# Append the third list to the first one and the fourth list to the second none
# Extend the first list with the help of the fifth list and the second one with the help auf the sixth list#

list_1 = list(range(5))
list_2 = list(range(3,11))
list_3 = list(range(5,12,2))
list_4 = list(range(8))
list_5 = list(range(2,12))
list_6 = list(range(7,16))

list_1.append(list_3)
print (list_1)

list_2.append(list_4)
print (list_2)

list_1.extend(list_5)
print (list_1)

list_2.extend(list_6)
print (list_6)
# index-1
print(list_4[-1]) #Gibt die letzte Zahl der Liste 4 aus
print(list_4[-2]) #Gibt die vorletzte Zahl aus und so weiter!
print (list_4[2:6]) # Gibt die Stellen 2-5 aus der Liste aus
print (list_4[2::]) #Gibt Stelle 2 bis zum Ende aus
print (list_4[:-3])
print (list_4[::3]) # Gibt alle Elemente an der dritten Stelle der Liste aus
