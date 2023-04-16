def retiraespaco(entrada):
    return entrada[1:]

def formatador(entrada):
    try:
        if entrada[-1] == '"' or entrada[-1] == '.':
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
    origem[entry[0]] = (entry[1]).split(',') 

for x in origem.keys():
    origem[x][-1] = formatador(origem[x][-1])
    if origem[x][-1] == country.lower():
        usuarios += 1

print('{} usuários de {}.'.format(usuarios,country))