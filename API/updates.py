import psycopg2
from connectbd import bd_config

def exec_update_livro(id_livro, novos_dados):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Cria uma string de atualização dinamicamente com base nos campos fornecidos
        update_query = "UPDATE lib.livro SET "
        update_values = []

        for campo, valor in novos_dados.items():
            update_query += f"{campo} = %s, "
            update_values.append(valor)

        update_query = update_query.rstrip(', ')
        update_query += f" WHERE id_livro = %s"
        update_values.append(id_livro)
        
        cursor.execute(update_query, update_values)
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na atualização do livro:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_update_autor(id_autor, novos_dados):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        update_query = "UPDATE lib.autor SET "
        update_values = []

        for campo, valor in novos_dados.items():
            update_query += f"{campo} = %s, "
            update_values.append(valor)

        update_query = update_query.rstrip(', ')
        update_query += f" WHERE id_autor = %s"
        update_values.append(id_autor)
        
        cursor.execute(update_query, update_values)
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na atualização do autor:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_update_livro_premiacao(id_livro, id_premiacao, novos_dados):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Cria uma string de atualização dinamicamente com base nos campos fornecidos
        update_query = "UPDATE lib.livro_premiacao SET "
        update_values = []

        for campo, valor in novos_dados.items():
            update_query += f"{campo} = %s, "
            update_values.append(valor)

        update_query = update_query.rstrip(', ')
        update_query += f" WHERE id_livro = %s AND id_premiacao = %s"
        update_values.extend([id_livro, id_premiacao])
        
        cursor.execute(update_query, update_values)
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na atualização do livro premiado:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()