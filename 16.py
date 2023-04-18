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
    try: #Algumas entradas nessa posição são textos, logo causam erros quando convertidos para int
        if int(entrada[3]) in ano_lista:
            #Converte o conteudo do indice 3 (Ano de publicação) para int e verifica se ele está na lista dos anos
            livros[entrada[0]] = [int(entrada[3]), 0]
            #Se estiver, cria uma chave no dicionario com o ISBN do livro e armazena uma lista contendo [Ano de publicação, 0]
    except:
        continue

arqRating = open('BX-Book-Ratings.csv', 'r', encoding='iso-8859-1')

for linha in arqRating:
    entrada = [retiraspas(x) for x in linha[:-1].split(";")]
    if entrada[1] in livros:
        #Verifica se [ISBN-TabelaRatings] corresponde a alguma chave no dicionario livros.
        livros[entrada[1]][1] = livros[entrada[1]][1] + 1
        #Se estiver, livros[ISBN][1] = livros[ISBN][1] + 1
        #Acessa o dicionario na chave ISBN, no indice 1, onde estamos armazenando o número de avaliações de cada livro

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