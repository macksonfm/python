#dado a lista
#times = ['time', ['Curintia', 'Palmeiras', 'Sao Paulo'], 'cores', ['Preto', 'Branco', 'Verde', 'Vermelho']]

#imprima na tela as seguintes mensagens:
#time: <nome_time>, cores: <cores_time>

# resultado esperado time: Curintia, cores: Preto, Braco
#print(f'O nome do usuario eh {nome}')
#print(lista[4][1])
# print(f'{times[0]}: {times[1][0]}, {times[2]}: {times[3][0]}, {times[3][1]}')
# print(f'{times[0]}: {times[1][1]}, {times[2]}: {times[3][2]}, {times[3][1]}')
# print(f'{times[0]}: {times[1][2]}, {times[2]}: {times[3][3]}, {times[3][0]}, {times[3][1]}')



# dado o dicionario:


dados = {
    'estados': {
        'sp':{
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg':{
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }

}

# Imprima as seguintes informações:

# 1. Nome dos estados
print(dados['estados']['sp']['nome'])


# 2. Nome dos estados, quantidade de municipios e  população
print(f"Nome: {dados['estados']['sp']['nome']}")