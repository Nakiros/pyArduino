def operatii(x, y):
    suma = x+y
    diferenta = x-y
    prod = x*y
    divi = x/y
    return suma, round(diferenta, 2), round(prod, 2), round(divi, 2)


a = float(input('Please input your first number: '))
b = float(input('Please input your second number: '))
alfa, beta, delta, gama = operatii(a, b)
print('Suma:', alfa)
print('Diferenta:', beta)
print('Produs:', delta)
print('Divizare:', gama)
