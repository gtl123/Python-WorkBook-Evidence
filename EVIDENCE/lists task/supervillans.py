super_villains = ['Magneto', 'Joker', 'Doctor Doom', 'Lex Luthor']
wages = [21, 17, 3, 5]
totalWage = 0

for i in range(len(super_villains)):
    print(super_villains[i] + ': £' + str(wages[i]) + ' million')

for wage in wages:
    totalWage += wage

print('Total wage bill for the League: £' + str(totalWage) + ' million')