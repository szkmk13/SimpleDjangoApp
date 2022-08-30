from random import choice

osoby = ['Szymon Kowalski', 'Krzystof Skibicki', 'Wiktoria Kwiatkowska', 'osoba', 'Kamil Galicki',
         'Agnieszka Horodecka', 'Bartosz Wojnar','Agnieszka Aksmann', 'Joanna Starosta', 'Ania Sarwińska',
         'Damian Fierka', 'Michał Pawlak', 'Martyna Maląg','Łukasz Wilamowski','Klaudia Gajdzińska']
g1 = []
g2 = []
g3 = []
x = 0
print("wszyscy:"),print(osoby)
while len(osoby) > 0:
    x = choice(osoby)
    g1.append(x)
    osoby.remove(x)

    x = choice(osoby)
    g2.append(x)
    osoby.remove(x)

    x = choice(osoby)
    g3.append(x)
    osoby.remove(x)

print(g1)
print(g2)
print(g3)
