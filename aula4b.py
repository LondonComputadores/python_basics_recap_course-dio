for num in range(101):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        #print(x, resto) #comentar essa linha para testar e ver diferença de resultados
        if resto == 0:
            div += 1

    if div == 2:
        print(num)