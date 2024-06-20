from codigo.conexao import colecao
from bson.objectid import ObjectId

def inserir_livro(titulo, autor, ano_publicacao, genero, num_paginas, sinopse, isbn):
    from codigo.validacao import validar_ano, validar_num_paginas

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
