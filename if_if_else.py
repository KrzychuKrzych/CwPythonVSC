print('podaj a i b: ')
a = int(input())
b = int(input())

if a > 0 and b > 0:
    if a % 2 == 0 or b % 2 == 0:
        print('Warunki spełnione')
    else:
        print('Żadna z liczb nie jest parzysta')
else:
    print('Conajmniej jedna z liczb nie jest dodatnia')