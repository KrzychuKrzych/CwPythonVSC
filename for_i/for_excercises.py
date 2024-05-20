#numbers = [2,5,13,14,15,16]

#square = []
#for number in numbers:
#    square.append(number * 2)

#print(square)

#for number in range(2,21):
#    is_first = True
#    for i in range(2, int(number ** 0.5) + 1):
#        if number % i == 0:
#            is_first = False
#            break
#    if is_first:
#        print(number, end=",")

cities = ['Gd', 'WWa', 'Pz']
cities_reversed = []

for city in reversed(cities):
    cities_reversed.append(city)
    
print(cities_reversed)