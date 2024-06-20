from pymongo import MongoClient
from bson.objectid import ObjectId
import re

# Configuração do cliente MongoDB
client = MongoClient('localhost', 27017)
db = client['biblioteca']
colecao = db['livros']

# Funções de Validação

def validar_ano(ano):
    try:
        ano = int(ano)
        if ano <= 0 or ano > 2024:
            return False
        return True
    except ValueError:
        return False

def validar_num_paginas(num_paginas):
    try:
        num_paginas = int(num_paginas)
        if num_paginas > 0:
            return True
        return False
    except ValueError:
        return False

# Funções CRUD

def inserir_livro(titulo, autor, ano_publicacao, genero, num_paginas, sinopse, isbn):
    if not validar_ano(ano_publicacao):
        print("Ano de publicação inválido. Certifique-se de inserir um ano válido, por exemplo: 1990.")
        return
    if not validar_num_paginas(num_paginas):
        print("Número de páginas inválido. Certifique-se de inserir um número positivo.")
        return

    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano_publicacao': ano_publicacao,
        'genero': genero,
        'num_paginas': num_paginas,
        'sinopse': sinopse,
        'isbn': isbn
    }
    resultado = colecao.insert_one(livro)
    print(f"Livro inserido com o ID: {resultado.inserted_id}")

def atualizar_livro_por_titulo(titulo, novos_valores):
    resultado = colecao.update_many(
        {'titulo': {'$regex': titulo, '$options': 'i'}},
        {'$set': novos_valores}
    )
    if resultado.modified_count > 0:
        print(f"{resultado.modified_count} livro(s) com o título '{titulo}' atualizado(s) com sucesso.")
    else:
        print(f"Nenhum livro encontrado com o título '{titulo}'. Nenhuma alteração foi feita.")

def deletar_livro(titulo):
    resultado = colecao.delete_many({'titulo': {'$regex': titulo, '$options': 'i'}})
    if resultado.deleted_count > 0:
        print(f"{resultado.deleted_count} livro(s) com o título '{titulo}' deletado(s) com sucesso.")
    else:
        print(f"Nenhum livro encontrado com o título '{titulo}'. Nenhuma exclusão foi feita.")

def listar_livros_por_autor(autor):
    return list(colecao.find({'autor': autor}))

def listar_livros_por_genero(genero):
    return list(colecao.find({'genero': genero}))

def listar_livros_por_ano(ano):
    return list(colecao.find({'ano_publicacao': ano}))

def listar_10_livros_mais_paginas():
    return list(colecao.find().sort('num_paginas', -1).limit(10))

def listar_10_livros_menos_paginas():
    return list(colecao.find().sort('num_paginas', 1).limit(10))

def buscar_livro_por_isbn(isbn):
    livro = colecao.find_one({'isbn': isbn})
    if livro:
        return livro
    else:
        print("Livro não encontrado para o ISBN fornecido.")
        return None

def buscar_livro_por_titulo(titulo):
    livros = list(colecao.find({'titulo': {'$regex': titulo, '$options': 'i'}}))
    if livros:
        return livros
    else:
        print("Nenhum livro encontrado para o título fornecido.")
        return []

def listar_todos_os_livros():
    return list(colecao.find({}, {'titulo': 1, 'autor': 1}))

# Funções de utilidade para exibição

def exibir_livro(livro):
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano de Publicação: {livro['ano_publicacao']}")
    print(f"Gênero: {livro['genero']}")
    print(f"Número de Páginas: {livro['num_paginas']}")
    print(f"Sinopse: {livro['sinopse']}")
    print(f"ISBN: {livro['isbn']}\n")

def exibir_titulos_autores(livros):
    for livro in livros:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}")

# Menu interativo

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir livro")
        print("2. Atualizar livro")
        print("3. Deletar livro")
        print("4. Listar livros por autor")
        print("5. Listar livros por gênero")
        print("6. Listar livros por ano de publicação")
        print("7. Listar os 10 livros com mais páginas")
        print("8. Listar os 10 livros com menos páginas")
        print("9. Buscar livro por ISBN")
        print("10. Buscar livro por título")
        print("11. Listar todos os livros (apenas título e autor)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = input("Ano de Publicação: ")
            genero = input("Gênero: ")
            num_paginas = input("Número de Páginas: ")
            sinopse = input("Sinopse: ")
            isbn = input("ISBN: ")
            inserir_livro(titulo, autor, ano_publicacao, genero, num_paginas, sinopse, isbn)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '2':
            titulo = input("Título do livro a ser atualizado: ")
            while True:
                campo = input("Campo a ser atualizado (titulo, autor, ano_publicacao, genero, num_paginas, sinopse) ou 0 para voltar ao menu: ")
                if campo == '0':
                    break
                novo_valor = input(f"Novo valor para {campo}: ")
                atualizar_livro_por_titulo(titulo, {campo: novo_valor})
                input("Aperte 0 para voltar ao menu: ")

        elif opcao == '3':
            titulo = input("Título do livro a ser deletado: ")
            deletar_livro(titulo)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '4':
            autor = input("Autor: ")
            livros = listar_livros_por_autor(autor)
            for livro in livros:
                exibir_livro(livro)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '5':
            genero = input("Gênero: ")
            livros = listar_livros_por_genero(genero)
            for livro in livros:
                exibir_livro(livro)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '6':
            ano = input("Ano de Publicação: ")
            if validar_ano(ano):
                livros = listar_livros_por_ano(int(ano))
                for livro in livros:
                    exibir_livro(livro)
            else:
                print("Ano de publicação inválido. Certifique-se de inserir um ano válido, por exemplo: 1990.")
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '7':
            livros = listar_10_livros_mais_paginas()
            for livro in livros:
                exibir_livro(livro)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '8':
            livros = listar_10_livros_menos_paginas()
            for livro in livros:
                exibir_livro(livro)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '9':
            isbn = input("ISBN: ")
            livro = buscar_livro_por_isbn(isbn)
            if livro:
                exibir_livro(livro)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '10':
            titulo = input("Título: ")
            livros = buscar_livro_por_titulo(titulo)
            for livro in livros:
                exibir_livro(livro)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '11':
            livros = listar_todos_os_livros()
            exibir_titulos_autores(livros)
            input("Aperte 0 para voltar ao menu: ")

        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
