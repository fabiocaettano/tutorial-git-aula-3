def potencia(a,b):
    
    potencia = 1
    count = 1

    while count <= b:
        potencia *= a
        count = count + 1

    print(f"{a} ^ {b} = {potencia}")

potencia(10,5)