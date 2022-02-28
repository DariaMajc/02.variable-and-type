#Stwórz zmienną przechowującą wyraz o długości
#nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

name = 'Ignacekek'
name_lenght = len(name)//2
first_center = name_lenght - 1
second_center = name_lenght + 1
print(name[first_center:second_center + 1])

#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
#utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'kiwi'
s2 = 'melon'
s3 = s1[0:2]
print(s3+s2)

quote = 'Honesty is the first chapter in the book of wisdom.'

#Policz wszystkie znaki w napisie
print(len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])

# Wyświetl tylko pierwszą połowę tekstu
print(quote[:24])

# Wyświetl tylko kropkę
print(quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[24::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])

# Wyświetl cały cytat odwrotnie
print(quote[::-1])

# Zamień wisdom na słowo friendship
print(quote[:-8], 'friendship.')
