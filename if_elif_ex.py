print('Podaj ilość punktów: ')
pkt = input()
print('Twoje punkty to: ' + pkt)

if pkt >= '90':
    print('A')
elif pkt >= '80':
    print('B')
elif pkt >= '70':
    print('C')
elif pkt >= '60':
    print('D')
else:
    print('F')
