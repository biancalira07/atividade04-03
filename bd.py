import sqlite3


def criar():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor() 

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS biblioteca (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(55) NOT NULL,
            autor VARCHAR(20) NOT NULL,
            paginas INT NOT NULL,
            genero VARCHAR ( 20) NOT NULL);
    """) 

    conn.close()


def novo_livro(nome, autor, paginas, genero):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor() 

    cursor.execute("""
        INSERT INTO biblioteca (nome, autor, paginas, genero)
        VALUES(nome, autor, paginas, genero);
    """) 
    conn.commit()
    conn.close()


def listar_livro():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM biblioteca")
    resultado = []
    for row in values:
        resultado.append({
            'id': row[0],
            'nome': row[1],
            'autor': row[2],
            'paginas': row[3],
            'genero' : row [4]
        })
    conn.close()
    return resultado


def atualiza_livro(id, nome, autor, paginas,genero):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE biblioteca 
        SET nome=?, autor=?, paginas=?, genero =?
        WHERE id=?;
        """,
        (nome, autor,paginas,genero, id)
    )
    conn.commit()
    conn.close()


def remover_livro(id):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM biblioteca 
        WHERE id=?;
        """,
        (id,)
    )
    conn.commit()
    conn.close()



def detalha_livro(id):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM biblioteca 
        WHERE id=?;
        """,
        (id,)
    )
    item = cursor.fetchone()
    conn.close()
    if item is None:
        return None
    return {
        'id': item[0],
        'nome': item[1],
        'autor': item[2],
        'paginas': item[3],
        'genero': item [4]
    }


if __name__=='__main__':
    criar()