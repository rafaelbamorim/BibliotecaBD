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
