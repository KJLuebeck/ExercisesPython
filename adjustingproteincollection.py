#Exercise 19 - Adjusting the Collection
#Write a program that allows the user to make changes with the dictionary from exercise 18

proteindictionary = {}
proteindictionary["Ferritin"] = {"Name":"Ferritin","Länge":"174/182 Aminosäuren (L/H)","Funktion":"Eisenspeicher","Location":"Leber, Milz, Knochenmark"}
proteindictionary["Bakterioferritin"] = {"Name":"Bakterioferritin","Länge":"lang","Funktion":"Eisenspeicher/unklar","Location":"Bakterien"}
proteindictionary["Myoglobin"] = {"Name":"Myoglobin","Länge":"153 Aminosäuren","Funktion":"Sauerstofftransport","Location":"Muskel"}
proteindictionary["Kollagen"] = {"Name":"Kollagen","Länge":"200-1000 Aminosäuren","Funktion":"Strukturprotein","Location":"Bindegewebe"}
proteindictionary["Hämoglobin"] = {"Name":"Hämoglobin","Länge":"141/146 Aminosäuren","Funktion":"Sauerstofftransport","Location":"Blut"}

print (proteindictionary) #druckt das gesamte dic incl aller Unterverzeichnisse
#print (proteindictionary["Ferritin"])#druckt das gesamte dic Ferritin, welches in proteindictionary enthalten ist
#print (proteindictionary["Ferritin"]["Name"]) #druckt Name aus dem dictionary Ferritin,welches in proteindictionary enthalten ist

#ask if user wants to add, delete or change an entry
no_1 = int(input("Do you want to add an entry (press 1), delete an entry (press 2) or change an entry (press 3)?\n"))
#add entry
if no_1 == 1:
    print ("Please give me some information about the protein you like to add.")
    key = input("Whats the name of the protein?")
    länge = input("Welche Länge hat dein Protein?")
    funktion = input ("Welche Funktion hat dein Protein?")
    location = input ("Wo befindet sich das Protein(Location)?")
    proteindictionary[key] = {"Name":key,"Länge":länge,"Funktion":funktion,"Location":location}
    print (proteindictionary)

#delete entry
if no_1 == 2:
    name_1 = input("Give me the name of the entry you want to delete:\n")
    del proteindictionary[name_1]
    print (proteindictionary)

#change entry
if no_1 == 3:
    name_1 = input("Give me the name of the entry you want to change:\n")
    print ("Which part do you want to change?")
    no_2 = int(input("1: Name 2: Länge 3: Funktion 4: Location"))
    if no_2 == 1:
        name_2 = input("Give me the new name for your protein\n")
        proteindictionary[name_1]["Name"] = name_1
        print(proteindictionary)
    if no_2 == 2:
        länge_2 = input("Give me the new length for your protein\n")
        proteindictionary[name_1]["Länge"] = länge_2
        print(proteindictionary)
    if no_2 == 3:
        funktion_2 = input("Give me the new function for your protein\n")
        proteindictionary[name_1]["Funktion"] = funktion_2
        print(proteindictionary)
    if no_2 == 4:
        location_2 = input("Give me the new location for your protein\n")
        proteindictionary[name_1]["Location"] = location_2
        print(proteindictionary)
