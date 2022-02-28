title = input('What is the title of the book? ')
author = input('Who is the author of the book? ')
pages = input('How many pages does this book have? ')

#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print(title.isalpha())
print(author.isalpha())
print(pages.isalnum())

#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print(title.title())
print(author.title())

#Połącz dane w jeden ciąg book za pomocą spacji
book = title + ' ' + author + ' ' + pages
print(book)

#Policz liczbę wszystkich znaków w napisie book
print(len(book))