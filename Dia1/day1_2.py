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

    sscore = sum((item1 * lista2.count(item1) for item1, item2 in zip(lista1, lista2)))
    print(sscore)
