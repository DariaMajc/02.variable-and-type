Zen_of_Python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#Policz liczbę wystąpień słowa better.
print(Zen_of_Python.count('better'))

print('----------------------------')
#Usuń z tekstu symbol gwiazdki
print(Zen_of_Python.replace("*", " "))

print('----------------------------')
#Zamień jedno wystąpienie explain na understand
replace = 'explain'
replace2 = 'understand'
print(Zen_of_Python.find(replace))
print(Zen_of_Python[:667], replace2, Zen_of_Python[677:])

print('----------------------------')
#Usuń spacje i połącz wszystkie słowa myślnikiem
Zen_of_Python2 = Zen_of_Python.replace(" ", "")
print("-".join(Zen_of_Python2))

print('----------------------------')
#Podziel tekst na osobne zdania za pomocą kropki
