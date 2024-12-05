with open('dados.txt','r') as arquivo:
    lista_arquivo = arquivo.readlines()

    lista1=[]
    lista2=[]

    for item in lista_arquivo:
        num1, num2 = item.strip().split('   ')
        lista1.append(int(num1))
        lista2.append(int(num2))
    lista1.sort()
    lista2.sort()

    res = 0
    
    distancia_total = sum(abs(item1 - item2) for item1, item2 in zip(lista1, lista2))

    print(distancia_total)
