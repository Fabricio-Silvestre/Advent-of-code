def verificar_seguranca(niveis):
    crescente = all(niveis[i] < niveis[i + 1] and 1 <= niveis[i + 1] - niveis[i] <= 3 for i in range(len(niveis) - 1))
    decrescente = all(niveis[i] > niveis[i + 1] and 1 <= niveis[i] - niveis[i + 1] <= 3 for i in range(len(niveis) - 1))
    return crescente or decrescente

with open('input2.txt', 'r') as arquivo:
    lista_arquivo = arquivo.readlines()

    
relatorios = []
for linha in lista_arquivo:
    niveis = list(map(int, linha.strip().split()))
    relatorios.append(niveis)

relatorios_seguros = 0
for relatorio in relatorios:
    relatorios_seguros += verificar_seguranca(relatorio)
print(f"Total de relatórios seguros: {relatorios_seguros}")

