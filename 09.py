def retiraspas(entrada):
    return entrada[1:-1]

def formatarISBN(entrada):
    if len(entrada) < 10:
        for x in range(10 - len(entrada)):
            entrada = '0' + entrada
    return entrada

print("Digite 2 livros e veja qual teve a pior avaliação média.")
tipo_pesquisa = -1

livro1 = ['','','',0,0,0] #isbn, titulo, ano, nota, quantidade, media
livro2 = ['','','',0,0,0]

notas = [0,0]
quantidade = [0,0]

while tipo_pesquisa > 2 or tipo_pesquisa < 1: #menu
        
    print("Como deseja pesquisar?")
    print("1 - Pesquisar por Título e Ano")
    print("2 - Pesquisar por ISBN")

    tipo_pesquisa = eval(input())

    if tipo_pesquisa == 1:
        livro1[1] = input("Digite o Título do primeiro livro: ")
        livro1[2] = input("Digite o Ano do primeiro livro: ")
        livro2[1] = input("Digite o Título do segundo livro: ")
        livro2[2] = input("Digite o Ano do segundo livro: ")

    elif tipo_pesquisa == 2:
        livro1[0] = input("Digite o ISBN do primeiro livro: ")
        livro2[0] = input("Digite o ISBN do segundo livro:  ")

    else: 
        print("Opção invalida, tente novamente!")

arqLivros = open('BX_Books.csv','r', encoding='iso-8859-1')

livro1[0] = formatarISBN(livro1[0])
livro2[0] = formatarISBN(livro2[0])

for linha in arqLivros:

    entrada = [retiraspas(x) for x in linha.split(";")]

    if tipo_pesquisa == 1:
        if livro1[1].lower() == (entrada[1]).lower() and livro1[2] == entrada[3]:
            livro1[0] = entrada[0]
        elif livro2[1].lower() == (entrada[1]).lower() and livro2[2] == entrada[3]:
            livro2[0] = entrada[0]
    else :
        if livro1[0].lower() == (entrada[0]).lower():
            livro1[1] = entrada[1]
        elif livro2[0].lower() == (entrada[0]).lower():
            livro2[1] = entrada[1]

arqAvaliacao = open('BX-Book-Ratings.csv', 'r', encoding='iso-8859-1')

for linha in arqAvaliacao:
    entrada = [retiraspas(x) for x in linha[:-1].split(";")]

    if livro1[0] == entrada[1]:
        livro1[3] = livro1[3] + int(entrada[2])
        livro1[4] = livro1[4] + 1

    elif livro2[0] == entrada[1]:
        livro2[3] = livro2[3] + int(entrada[2])
        livro2[4] = livro2[4] + 1
    
livro1[5] = livro1[3] / livro1[4]
livro2[5] = livro2[3] / livro2[4]

if livro1[5] > livro2[5]:
    print("O livro {} tem uma média mais baixa que {}".format(livro2[1], livro1[1]))

elif livro1[5] < livro2[5]:
    print("O livro {} tem uma média mais baixa que {}".format(livro1[1], livro2[1]))
else:
    print("Ambos os livros possuem a mesma média.")

print("O livro {} registrado no ISBN {} tem média {}.".format(livro1[1], livro1[0], livro1[5]))
print("O livro {} registrado no ISBN {} tem média {}.".format(livro2[1], livro2[0], livro2[5]))