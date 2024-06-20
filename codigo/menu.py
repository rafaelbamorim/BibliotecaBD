
from crud import (
    atualizar_livro_por_titulo, deletar_livro, listar_livros_por_autor,
    listar_livros_por_genero, listar_livros_por_ano, listar_10_livros_mais_paginas,
    listar_10_livros_menos_paginas, buscar_livro_por_isbn, buscar_livro_por_titulo,
    listar_todos_os_livros, inserir_livro
)
from codigo.validacao import validar_ano
from codigo.conexao import colecao


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