import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())

    return dados

def listar_categorias(dados: list) -> list: 
    '''
    O parâmetro "dados" é uma lista de dicionários que representa os produtos.
    Essa função retorna uma lista contendo todas as categorias dos diferentes produtos.
    '''
    categorias = []

    for dado in dados:
            if dado['categoria'] not in categorias:
                categorias.append(dado['categoria']) 

    return categorias 

def listar_por_categoria(dados: list, categoria: str) -> list:
    '''
    O parâmetro "dados" é lista de dicionários que representa os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função retorna uma lista contendo todos os produtos pertencentes à categoria desejada.
    '''
    lista_categorias = []

    for dado in dados:
        if dado["categoria"] == categoria:
            lista_categorias.append(dado) 

    return lista_categorias

def produto_mais_caro(dados: list, categoria: str) -> dict:
    '''
    O parâmetro "dados" é lista de dicionários que representa os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função retorna um dicionário representando o produto mais caro da categoria desejada.
    '''
    lista_categorias = listar_por_categoria(dados, categoria)
    mais_caro = sorted(lista_categorias, key=lambda x : float(x["preco"]), reverse=True)

    return mais_caro[0]


def produto_mais_barato(dados: list, categoria: str) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função retorna um dicionário com o produto mais caro da categoria dada.
    '''
    lista_categorias = listar_por_categoria(dados, categoria)
    mais_barato = sorted(lista_categorias, key=lambda x : float(x["preco"]))

    return mais_barato[0]

def top_10_caros(dados: list) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função retorna uma lista de dicionários com os 10 produtos mais caros.
    '''
    top_mais = sorted(dados, key=lambda x : float(x["preco"]), reverse = True)
    
    return top_mais[:10]

def top_10_baratos(dados: list) -> dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função retorna uma lista de dicionários com os 10 produtos mais baratos.
    '''
    top_menos = sorted(dados, key=lambda x : float(x["preco"]))
    
    return top_menos[:10]

def menu(dados: list) -> None:
    
    escolha = type(int)

    while escolha != 0:

        print('''
        **** OPÇÕES **** 
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
        ''')
        
        escolha = input("Escolha a opção desejada: ")

        while not(escolha.isdigit()):
            escolha = input("ATENÇÃO! Digite somente números: ")
        escolha = int(escolha)

        if escolha == 1: 
            for i in range(0,len(listar_categorias(dados))):
                print(f"{i+1} - {sorted(listar_categorias(dados))[i]}")

        elif escolha == 2:
            categoria = input("Insira a categoria desejada: ")
            lista_por_categoria = listar_por_categoria(dados,categoria)

            for i in range(0,len(lista_por_categoria)):
                print(f"id: {lista_por_categoria[i]['id']} | preço: R$ {lista_por_categoria[i]['preco']}")


        elif escolha == 3:
            categoria = input("Insira a categoria desejada: ")

            mais_caro = produto_mais_caro(dados, categoria)
            print(f'\nO produto com id: {mais_caro["id"]} é o mais caro da categoria {categoria}. \nNo valor de R$ {mais_caro["preco"]}')

        elif escolha == 4:
            categoria = input("Insira a categoria desejada: ")

            mais_barato = produto_mais_barato(dados, categoria)
            print(f'\nO produto com id: {mais_barato["id"]} é o mais barato da categoria {categoria}. \nNo valor de R$ {mais_barato["preco"]}')

        elif escolha == 5:    
            top10 = top_10_caros(dados)

            for i in range(0,10):    
                print(f'{i+1} - preço: R$ {top10[i]["preco"]} | id: {top10[i]["id"]} | categoria: {top10[i]["categoria"]}')
   
   
        elif escolha == 6:    
                    top10 = top_10_baratos(dados)

                    for i in range(0,10):    
                        print(f'{i+1} - preço: R$ {top10[i]["preco"]} | id: {top10[i]["id"]} | categoria: {top10[i]["categoria"]}')
       
        elif escolha == 0:

            print('\nFim...\nObrigado por utilizar.\n')

        else:
            print(f'\nATENÇÃO! Escolha inválida, escolha novamente!\n')

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)