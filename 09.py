#Dado dois livros X e Y, mostre qual deles tem a pior avaliação média.

def retiraspas(entrada):
    return entrada[1:-1]

def formatarISBN(entrada):
    #Para ter certeza que o ISBN dado pelo usuário para pesquisa
    #seja encontrado na tabelaBooks, é preciso corrigir o seu número
    #de caracteres para 10
    if len(entrada) < 10:
        for x in range(10 - len(entrada)):
            entrada = '0' + entrada
    return entrada

def menu(): #Menu
    pesquisa = -1
    while pesquisa != 1 and pesquisa != 2:
        print("Como deseja pesquisar?")
        print("1 - Pesquisar por Título e Ano")
        print("2 - Pesquisar por ISBN")
        try:
            pesquisa = eval(input())
            if pesquisa != 1 and pesquisa != 2:
                print("Opção invalida, tente novamente!")
        except:
            print("Opção invalida, tente novamente!")
    return pesquisa

print("Digite 2 livros e veja qual teve a pior avaliação média.")

tipo_pesquisa = -1
while tipo_pesquisa != 2 and tipo_pesquisa != 1:
    
    livro1 = ['','','',0,0,0] #isbn, titulo, ano, nota, quantidade, media   
    livro2 = ['','','',0,0,0] #isbn, titulo, ano, nota, quantidade, media

    tipo_pesquisa = menu()

    if tipo_pesquisa == 1:
        #Pesquisa por nome e ano. Como existem multiplos livros com mesmo ano e autor
        #É preciso pesquisar o ano para ter certeza do livro correto
        livro1[1] = input("Digite o Título do primeiro livro: ")
        livro1[2] = input("Digite o Ano do primeiro livro: ")
        livro2[1] = input("Digite o Título do segundo livro: ")
        livro2[2] = input("Digite o Ano do segundo livro: ")

    elif tipo_pesquisa == 2:
        #Pesquisa por id do livro (ISBN)
        livro1[0] = input("Digite o ISBN do primeiro livro: ")
        livro2[0] = input("Digite o ISBN do segundo livro:  ")

    arqLivros = open('BX_Books.csv','r', encoding='iso-8859-1')
    
    if tipo_pesquisa == 2:
        livro1[0] = formatarISBN(livro1[0])#Formata os ISBNs
        livro2[0] = formatarISBN(livro2[0])

    for linha in arqLivros:
        
        entrada = [retiraspas(x) for x in linha.split(";")]
        #recebe cada linha, transforma em lista, e retira as aspas

        if tipo_pesquisa == 1:
            if livro1[1].lower() == (entrada[1]).lower() and livro1[2] == entrada[3]: 
                #Se (Titulo-Input)(minusculo) == (Titulo-TabelaBooks)(minusculo) and (Ano-Input) == (Ano-TabelaBooks)
                livro1[0] = entrada[0]
                #Então, (ISBN-Input) = (ISBN-TabelaBooks)
            elif livro2[1].lower() == (entrada[1]).lower() and livro2[2] == entrada[3]:
                livro2[0] = entrada[0]
        else :
            if livro1[0].lower() == (entrada[0]).lower():
                #Se (ISBN-Input)(minusculo) == (ISBN-TabelaBooks)(minusculo)
                livro1[1] = entrada[1]
                #Então (Titulo-Input) = (Titulo-TabelaBooks)
            elif livro2[0].lower() == (entrada[0]).lower():
                livro2[1] = entrada[1]

    arqLivros.close()

    #Verifica se o livro/ISBN informado existe na Tabela
    #Em caso de não existir, Informa ao usuário e pede para tentar novamente
    if (livro1[1] == '' or livro1[0] == '') or (livro2[1] == '' or livro2[0] == ''):
        if tipo_pesquisa == 1:
            if livro1[1] == '' or livro1[0] == '':
                print('O livro \"{}\" informado, não foi encontrado.'.format(livro1[1]))
                print('Por favor, tente novamente!')
            if livro2[1] == '' or livro2[0] == '':
                print('O livro \"{}\" informado, não foi encontrado.'.format(livro2[1]))
                print('Por favor, tente novamente!') 
            tipo_pesquisa = -1

        elif tipo_pesquisa == 2:
            if livro1[1] == '' or livro1[0] == '':
                print('O ISBN \"{}\", não foi encontrado.'.format(livro1[0]))
                print('Por favor, tente novamente!')
            if livro2[1] == '' or livro2[0] == '':
                print('O ISBN \"{}\", não foi encontrado.'.format(livro2[0]))
                print('Por favor, tente novamente!')
            tipo_pesquisa = -1

    if tipo_pesquisa != -1:
        arqAvaliacao = open('BX-Book-Ratings.csv', 'r', encoding='iso-8859-1')

        for linha in arqAvaliacao:
            entrada = [retiraspas(x) for x in linha[:-1].split(";")]
            #recebe cada linha, transforma em lista, e retira as aspas. Ademais, retira 1 caractere extra no final.

            if livro1[0] == entrada[1]:
                #Se (ISBN-Input) == (ISBN-TabelaRating)
                livro1[3] = livro1[3] + int(entrada[2])
                #Então (nota-livro) = (nota-livro) + int(avaliação) ->Avaliação é uma str, por isso preciso transformar em int.
                livro1[4] = livro1[4] + 1
                #e (quantidade-avaliações) = (quantidade-avaliações) + 1

            elif livro2[0] == entrada[1]:
                livro2[3] = livro2[3] + int(entrada[2])
                livro2[4] = livro2[4] + 1
        
        arqAvaliacao.close()

        #Se um dos valores digitados, não for encontrado na tabela de avaliações.
        #Por isso, aqui estão as possibilidades de saida.
        if livro1[4] == 0 and livro2[4] == 0:
            print("Nenhum dos livros informados foi avaliado!")

        elif livro1[4] == 0 and livro2[4] != 0:
            print("Não houveram avaliações para o livro \"{}\", registrado no ISBN \"{}\".".format(livro1[1],livro1[0]))
            print("Enquanto o livro \"{}\" registrado no ISBN \"{}\" tem média {}.".format(livro2[1], livro2[0], livro2[5]))     

        elif livro2[4] == 0 and livro1[4] != 0:    
            print("Não houveram avaliações para o livro \"{}\", registrado no ISBN \"{}\".".format(livro2[1],livro2[0]))
            print("Enquanto o livro \"{}\" registrado no ISBN \"{}\" tem média {}.".format(livro1[1], livro1[0], livro1[5]))     

        else:
            livro1[5] = livro1[3] / livro1[4]
            # (Média-livro) = (nota-livro) / (quantidade-avaliações)
            livro2[5] = livro2[3] / livro2[4]

            if livro1[5] > livro2[5]: #Compara as médias e define qual teve a maior média.
                print("O livro \"{}\" tem uma média mais baixa que \"{}\"".format(livro2[1], livro1[1]))

            elif livro1[5] < livro2[5]:
                print("O livro \"{}\" tem uma média mais baixa que \"{}\"".format(livro1[1], livro2[1]))
            else:
                print("Ambos os livros possuem a mesma média.")

            print("O livro \"{}\" registrado no ISBN \"{}\" tem média {}.".format(livro1[1], livro1[0], livro1[5]))
            print("Enquanto livro \"{}\" registrado no ISBN \"{}\" tem média {}.".format(livro2[1], livro2[0], livro2[5]))