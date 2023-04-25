#Mostre o X ano que teve mais avaliações com um intervalo entre X e Y.
#Recebe o intervalo de anos e imprime o ano com mais avaliações desse intervalo.
#Ex: Entre 2000 e 2005, define qual teve a maior quantidade de avaliações e imprime.

def retiraspas(entrada):
    return entrada[1:-1]

print('Descubra o ano com mais avaliações em um período')
ano_inicial = input("Digite o ano de inicio do período: ")
ano_final = input("Digite o ano final do período: ")

if ano_final < ano_inicial: #Corrige a ordem de inicio e fim do periodo, caso esteja incorreta
    ano_inicial,ano_final = ano_final,ano_inicial

ano_lista = []
quant_dict = {}
livros = {}

for x in range((int(ano_final) - int(ano_inicial))+1):
    #Define cada ano, no perído escolhido pelo usuário
    ano_lista.append(int(ano_inicial) + x)
    #Adiciona cada ano a lista contendo os anos
    quant_dict[int(ano_inicial) + x] = 0
    #Cria chaves para o dicionario com os anos

arqLivros = open('BX_Books.csv', 'r', encoding='iso-8859-1')

for linha in arqLivros:

    entrada = [retiraspas(x) for x in linha.split(";")]
    #Cria chaves para o dicionario livros, com o ISBN dos livros
    #E cria uma lista para corresponder casa chave, [ano, quantidade de avaliações]
    #Alguns casos, o ano está contido no indice 3, em outros no indice 4.
    #Identifica, qual desses é o ano e adiciona a lista.
    if len(entrada[3]) > 4:
        try:
            temp = int(entrada[4])
            if temp in ano_lista:
                livros[entrada[0]] = [temp, 0]
        except:
            continue
    else:
        try:
            temp = int(entrada[3])
            if temp in ano_lista:
                livros[entrada[0]] = [temp, 0]
        except:
            continue

arqLivros.close

arqRating = open('BX-Book-Ratings.csv', 'r', encoding='iso-8859-1')

for linha in arqRating:
    entrada = [retiraspas(x) for x in linha[:-1].split(";")]
    if entrada[1] in livros:
        #Verifica se [ISBN-TabelaRatings] corresponde a alguma chave no dicionario livros.
        livros[entrada[1]][1] = livros[entrada[1]][1] + 1
        #Se estiver, livros[ISBN][1] = livros[ISBN][1] + 1
        #Acessa o dicionario na chave ISBN, no indice 1, onde estamos armazenando o número de avaliações de cada livro
arqRating.close()

for indice in livros.keys():
    #cria um laço de repetição com as chaves do dicionario livros.
    quant_dict[livros[indice][0]] = quant_dict[livros[indice][0]] + livros[indice][1]
    #quant_dict[livros[ISBN][Ano de Publicação]] = quant_dict[livros[ISBN][Ano de Publicação]] + livros[ISBN][número de avaliações]
    #Acessa o dicionario quant_dict na chave do ano e atualiza o valor, com base no número de avaliações armazenado no dicionario livros

maior = 0
for x in quant_dict.values():
    if x >= maior:
        maior = x
    #identifica qual o maior número de avaliações contido no dicionario quant_dict

for x in quant_dict.keys():
    #Procura qual chave, possui o maior número de avaliações, encontrado na pesquisa anterior
    if quant_dict[x] == maior:
        #imprime o ano com o maior número de avalições e a quantidade.
        print("O ano com mais avaliações no período é: {}.".format(x))
        print("Com um total de {} avaliações.".format(maior))