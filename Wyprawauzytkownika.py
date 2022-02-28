distance = input('Podaj dystans wyprawy w km ')
distance = int(distance)
usage = input('Podaj zużycie paliwa na 100 km w Twoim samochodzie ')
usage = float(usage)
petrol_price = 5.04

cost_of_trip = round(distance * petrol_price * usage, 2)

print(f'Koszt Twojej wyprawy wynosi: { cost_of_trip } zł')
