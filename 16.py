def retiraspas(entrada):
    return entrada[1:-1]

print('Descubra o ano com mais avaliações em um período')
ano_inicial = input("Digite o ano de inicio do período: ")
ano_final = input("Digite o ano final do período: ")

ano_lista = []
quant_dict = {}
livros = {}

for x in range((int(ano_final) - int(ano_inicial))+1):
    ano_lista.append(int(ano_inicial) + x) 
    quant_dict[int(ano_inicial) + x] = 0

arqLivros = open('BX_Books.csv', 'r', encoding='iso-8859-1')

for linha in arqLivros:

    entrada = [retiraspas(x) for x in linha.split(";")]
    try:
        if int(entrada[3]) in ano_lista:
            livros[entrada[0]] = [int(entrada[3]), 0]
    except:
        continue

arqRating = open('BX-Book-Ratings.csv', 'r', encoding='iso-8859-1')

for linha in arqRating:
    entrada = [retiraspas(x) for x in linha[:-1].split(";")]
    if entrada[1] in livros:
        livros[entrada[1]][1] = livros[entrada[1]][1] + 1

for indice in livros.keys():
    quant_dict[livros[indice][0]] = quant_dict[livros[indice][0]] + livros[indice][1]

maior = 0
for x in quant_dict.values():
    if x >= maior:
        maior = x

for x in quant_dict.keys():
    if quant_dict[x] == maior:
        print("O ano com mais avaliações no período é: {}.".format(x))
        print("Com um total de {} avaliações.".format(maior))