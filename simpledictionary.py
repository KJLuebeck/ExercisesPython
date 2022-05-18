# Exercise 16 - Simple dictionary
# Write a program that generates a simple dictionary consisting of at least
# three pre-defined entries with biological or biochemical background
dictionary_1={"Tier":"Wal", "Pflanze":"Löwenzahn", "Bakterium":"E.coli"}
#dictionary_1["Pilz"] = "Fliegenpilz"
print (dictionary_1)

# Ask the user for an entry that should be removed and remove the entry from the dictionary
newentrykey = input("Give me a new entry for my super dictionary!\nKey?")
newentryvalue =input("Value?")
dictionary_1[newentrykey]=newentryvalue
print (dictionary_1)

deleteentry = input("Which entrykey do you want to remove from my super dictionary?")
if deleteentry in dictionary_1:
    del dictionary_1 [deleteentry]
    print (dictionary_1)
else:
    print ("Fail")
# Print out the remaining dictionary
search = input("Give me a key to lookup in the dictionary")
if search in dictionary_1:
    print(f"Its in the dictionary {dictionary_1[search]}")
else:
    print ("Fail") 
