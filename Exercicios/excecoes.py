# dada a lista

funcionarios = ['joao', 'maria', 'carlos', 'paula', 'mario', 'frodo']

# faça um programa que valide se o usuario é funcionario
# caso seja
# imprima acesso permitido
# caso não
# imprima acesso negado
# sendo que o funcionario frodo está bloqueado
# caso ele tente entrar será exibido um NameError com a seguinte mensagem
# Usuario bloqueado, ir direto pro RH

while True:
    try:
        usuario = input('Digite seu nome: ')
        if usuario in funcionarios:
            if usuario == 'frodo':
                raise NameError('Usuario bloqueado, ir direto pro RH')
            else:
                print('Acesso Permitido')
                break
        else:
            raise ValueError('Acesso negado')

    except NameError as bloqueado:
        print(bloqueado)
        break
    except ValueError as negado:
        print(negado)
        continue


