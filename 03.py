def formatador(entrada):
    #Definição de Função para formatar o país, recebendo da tabela
    #Como existem países que tem um caracter extra fora do alfabeto, como "" ou .
    #A primeira parte avalia se o ultimo caractere pertence ao alfabeto, a partir de seu número na tabela ASCII
    #Em caso afirmativo, elimina esse caractere
    #Ademais, é retirado o espaço em branco presente no inicio de todas as entradas
    try:
        if ord(entrada[-1]) >= 97 or ord(entrada[-1]) <= 122:
            return entrada[1:-1]
        else:
            return entrada[1:]
    except:
        return None

country = input('Qual país você quer saber o número de usuários: ')
usuarios = 0
origem = {}

tabelaUsuario = open('BX-Users.csv', 'r', encoding='iso-8859-1')

for linha in tabelaUsuario:
    entry = linha.split(';')
    #O dicionario origem recebe a chave contida no indice 0(User-ID) da lista entry
    #E recebe como valor, uma lista, contendo o conteudo do indice 1(Location)
    origem[entry[0]] = (entry[1]).split(',') 

for x in origem.keys():
    origem[x][-1] = formatador(origem[x][-1])
    #A partir da lista armazenada anteriormente, utiliza da função formatador
    #no último elemento, onde fica armazenado o país.
    if origem[x][-1] == country.lower():
        #Compara o país do usuário com o país recebido como entrada
        #A função .lower() deixa todos os caracteres da palavra minusculos
        usuarios += 1
        #Em caso dos paises serem iguais, é aumentado 1 unidade na variável usuários

print('{} usuários de {}.'.format(usuarios,country))