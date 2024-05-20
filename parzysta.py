#print('podaj liczbe')
#number = int(input())

#if number % 2 == 0:
#    print('Liczba jest parzysta')
#else:
#    print('Liczba jest nieparzysta')
    
    
#if number % 2 == 0 and 0 < number < 20 :
#    print('Dodatnia, parzysta i mniejsza od 20')
#else:
#    print('Inna')
    
#print('podaj wyraz')
#word = str(input())

#if len(word) > 5:
#    print('Dłuższy niż 5 znaków')
#else:
#    print('krótszy niż 5 znaków')

print('podaj a i b: ')
a = input()
b = input()

if a == b:
    print('równe')
else:
    print('nierówne')
    
print('podaj a i b: ')
a = input()
b = input()

if a > 0 and b > 0:
    if a % 2 == 0 or b % 2 == 0:
        print('Jedna z liczb jest parzysta')
else:
    print('Liczba z poza zakresu')