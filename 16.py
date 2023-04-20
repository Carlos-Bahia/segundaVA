#Mostre o X ano que teve mais avaliações com um intervalo entre X e Y.

def retiraspas(entrada):
    return entrada[1:-1]

#Recebe as notas de incio e fim do período
intervaloA = int(input('Digite o inicio do intervalo: '))
while intervaloA < 0 or intervaloA > 10:
    print('Valor de Inicio do Intervalo está fora do alcance: 0 - 10')
    intervaloA = int(input('Por favor escolha outro valor: '))
intervaloB = int(input('Digite o fim do intervalo: '))
while intervaloB < 0 or intervaloB > 10:
    print('Valor Final do Intervalo está fora do alcance: 0 - 10')
    intervaloB = int(input('Por favor escolha outro valor: '))

if intervaloA > intervaloB:#Corrige o inicio e o fim do intervalo de notas, se necessário
    intervaloA,intervaloB = intervaloB,intervaloA

intervalo = []
anos = []
quantAnos = {}
livros = {}

for x in range((intervaloB - intervaloA)+1):
    #Cria uma lista contendo todas as possibilidades de nota, entre o inicio e o fim do intervalo.
    intervalo.append(intervaloA + x)

arqLivros = open('BX_Books.csv', encoding='iso-8859-1')
arqLivros.readline()

for linha in arqLivros:
    entrada = [retiraspas(x) for x in linha.split(";")]
    #Cria uma lista com os anos los livros da lista.
    #Alguns casos, está contido no indice 3, em outros no indice 4.
    #Identifica, qual desses é o ano e adiciona a lista.
    if len(entrada[3]) > 4:
        try:
            temp = int(entrada[4])
            livros[entrada[0]] = [temp,0]
            if temp not in anos:
                anos.append(temp)
        except:
            continue
    else:
        try:
            temp = int(entrada[3])
            livros[entrada[0]] = [temp,0]
            if temp not in anos:
                anos.append(temp)
        except:
            continue

listaAnos = sorted(anos)

arqLivros.close()

arqAvaliacoes = open('BX-Book-Ratings.csv', encoding='iso-8859-1')
arqAvaliacoes.readline()

for linha in arqAvaliacoes:
    entrada = [retiraspas(x) for x in linha[:-1].split(";")]
    if int(entrada[2]) in intervalo:
    #Se (nota-avaliação) estiver dentro do intervalo de notas desejado:
        try:
        #Tente adicionar 1 ao contador do livro.
            livros[entrada[1]][1] += 1
            #livros[ISBN][contador] adicione 1.
        except KeyError:
        #Alguns livros estão presentes na tabela de Livros(BX-Books.csv), mas não
        #estão presentes na tabela de avaliações(BX-Books-Ratings.csv).
        #Por isso, algumas chaves do dicionario livro, não existem e apresentam KeyError.
            continue
arqAvaliacoes.close()

for x in listaAnos:
    quantAnos[x] = [0]
    #Inicia o dicionario quantAnos, com uma lista de um elemento = 0.
    #Tendo como chave, os anos dos livros

for x in livros.keys():
    quantAnos[int(livros[x][0])][0] = quantAnos[int(livros[x][0])][0] + livros[x][1]
    #quantAnos[ano][contador] = quantAnos[ano][contador] + livros[ISBN][contador]     
    #Acessa o dicionario quantAnos na chave, gravada no indice 0(ano), de cada chave no dicionario livros.
    
maisAvalicoes = 0
for x in quantAnos.values():
    #identifica o maior número de avalições registrado em todos os anos
    if x[0] > maisAvalicoes:
        maisAvalicoes = x[0]

for x in quantAnos.keys():
    #Identifica o ano com mais avaliações e imprime na tela.
    if quantAnos[x][0] == maisAvalicoes:
        print("Livros do ano {} tiveram mais avaliações entre {} e {}.".format(x, intervaloA, intervaloB))
        print("Com um total de {} avaliações.".format(maisAvalicoes))

#print(quantAnos)