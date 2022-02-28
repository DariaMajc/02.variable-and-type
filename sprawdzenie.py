masa = input('Podaj wage [kg]')
masa = int(masa)

wzrost = input('Podaj wzrost [m]')
wzrost = float(wzrost)

bmi = masa / (wzrost ** 2)
print('Your BMI =', bmi)