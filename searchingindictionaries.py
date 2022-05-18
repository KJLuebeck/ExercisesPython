# Exercise 17 - Searching in dictionaries

dictionary_1 = {"Giraffe":"6 m","Elefant":"4 m","Tiger":"3.7 m","Eisbär":"3.5 m","Elch":"3.1 m","Grizzlybär":"2.9 m","Strauß":"2.8 m","Blauwal":"30 m"}
dictionary_1_copy = dictionary_1.copy()

search_1 = input("Welches Tier möchtest du im Buch der größten Tiere nachsehen?")
if search_1 in dictionary_1:
    print(f"Hier ist es und es ist {dictionary_1[search_1]}groß!")
    entry_1 =input("Bitte bring den Eintrag auf den neuesten Stand!")
    dictionary_1[search_1]=entry_1
    print(f"Hier mein ursprüngliches Buch der riesigen Tiere{dictionary_1_copy}")
    print(f"Hier die verbesserte Neuauflage{dictionary_1}")

else:
    print ("Das war wohl nichts! Lass uns einen neuen Eintrag machen!")
    newentryvalue =input("Wie groß ist es?")
    dictionary_1[search_1]=newentryvalue
    print(f"Hier mein ursprüngliches Buch der riesigen Tiere{dictionary_1_copy}")
    print(f"Hier die verbesserte Neuauflage{dictionary_1}")

search_1 = input("Welches Tier möchtest du im Buch der größten Tiere nachsehen?")
if search_1 in dictionary_1:
    print(f"Hier ist es und es ist {dictionary_1[search_1]}groß!")
    entry_1 =input("Bitte bring den Eintrag auf den neuesten Stand!")
    dictionary_1[search_1]=entry_1
    print(f"Hier mein ursprüngliches Buch der riesigen Tiere{dictionary_1_copy}")
    print(f"Hier die verbesserte Neuauflage{dictionary_1}")

else:
    print ("Das war wohl nichts! Lass uns einen neuen Eintrag machen!")
    newentryvalue =input("Wie groß ist es?")
    dictionary_1[search_1]=newentryvalue
    print(f"Hier mein ursprüngliches Buch der riesigen Tiere{dictionary_1_copy}")
    print(f"Hier die verbesserte Neuauflage{dictionary_1}")

search_1 = input("Welches Tier möchtest du im Buch der größten Tiere nachsehen?")
if search_1 in dictionary_1:
    print(f"Hier ist es und es ist {dictionary_1[search_1]}groß!")
    entry_1 =input("Bitte bring den Eintrag auf den neuesten Stand!")
    dictionary_1[search_1]=entry_1
    print(f"Hier mein ursprüngliches Buch der riesigen Tiere{dictionary_1_copy}")
    print(f"Hier die verbesserte Neuauflage{dictionary_1}")

else:
    print ("Das war wohl nichts! Lass uns einen neuen Eintrag machen!")
    newentryvalue =input("Wie groß ist es?")
    dictionary_1[search_1]=newentryvalue
    print(f"Hier mein ursprüngliches Buch der riesigen Tiere{dictionary_1_copy}")
    print(f"Hier die verbesserte Neuauflage{dictionary_1}")
