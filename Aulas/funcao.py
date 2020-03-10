# -*- Coding: Utf-8 -*-

# def soma(x, y):
#     return x + y

# print(soma(10, 11))

produtos = []

def cadastrar_produto(produto):
    global produtos
    produtos.append(produto)

def listar_produtos():
    global produtos
    for p in produtos:
        print(p)


def deleta_produto():
    global produtos
    produtos.remove(produto)

    




cadastrar_produto('abacaxi')
cadastrar_produto('limao')
cadastrar_produto('laranja')
listar_produtos()
