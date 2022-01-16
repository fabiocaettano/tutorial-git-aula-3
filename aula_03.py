def divide(a,b):
    print(f"{a} dividido por {b} é igual a {a/b}.")

def subtrair(a,b):
    print(f"{a} - {b} = {a-b}.")

def soma(a,b):
    print(f"{a} + {b} = {a+b}")

def multiplicar(a,b):
    print(f"{a} * {b} = {a*b}")

def potencia(a,b):
    
    potencia = 1
    count = 1

    while count <= b:
        potencia *= a
        count = count + 1

    print(f"{a} ^ {b} = {potencia}")

divide(10,5)
soma(10,5)
subtrair(10,5)
multiplicar(10,5)
potencia(10,5)