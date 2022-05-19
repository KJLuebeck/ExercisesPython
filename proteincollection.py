# Exercise 18 - Protein Collection
# Write a program that creates a complex dictionary in form of a protein collection
# Each entry of the dictionary "proteins" should contain another dictionary in which the name, the lenght
# and the function and location are collected
#information about at least five proteins
#print out the final dictionary at the endpoint

proteindictionary = {}
proteindictionary["Ferritin"] = {"Name":"Ferritin","Länge":"174/182 Aminosäuren (L/H)","Funktion":"Eisenspeicher","Location":"Leber, Milz, Knochenmark"}
proteindictionary["Bakterioferritin"] = {"Name":"Bakterioferritin","Länge":"lang","Funktion":"Eisenspeicher/unklar","Location":"Bakterien"}
proteindictionary["Myoglobin"] = {"Name":"Myoglobin","Länge":"153 Aminosäuren","Funktion":"Sauerstofftransport","Location":"Muskel"}
proteindictionary["Kollagen"] = {"Name":"Kollagen","Länge":"200-1000 Aminosäuren","Funktion":"Strukturprotein","Location":"Bindegewebe"}
proteindictionary["Hämoglobin"] = {"Name":"Hämoglobin","Länge":"141/146 Aminosäuren","Funktion":"Sauerstofftransport","Location":"Blut"}

print (proteindictionary) #druckt das gesamte dic incl aller Unterverzeichnisse
print (proteindictionary["Ferritin"])#druckt das gesamte dic Ferritin, welches in proteindictionary enthalten ist
print (proteindictionary["Ferritin"]["Name"]) #druckt Name aus dem dictionary Ferritin,welches in proteindictionary enthalten ist
