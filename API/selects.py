import psycopg2
from connectbd import bd_config

def exec_select_livro(): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # consulta na tabela livro
        cursor.execute("SELECT * FROM lib.livro ORDER BY id_livro")
        results = cursor.fetchall()

        col_names = [desc[0] for desc in cursor.description]    # pega o nome das colunas

        # lista de dicionários ordenada
        format_results = []
        for row in results:
            formatted_result = {
                "id_livro": row[col_names.index("id_livro")],
                "isbn": row[col_names.index("isbn")],
                "titulo": row[col_names.index("titulo")],
                "ano_publicacao": row[col_names.index("ano_publicacao")],
                "sinopse": row[col_names.index("sinopse")],
                "id_autor": row[col_names.index("id_autor")],
                "id_editora": row[col_names.index("id_editora")]
            }
            format_results.append(formatted_result)
        
        return format_results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_select_autor(): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # consulta na tabela autor
        cursor.execute("SELECT * FROM lib.autor ORDER BY id_autor")
        results = cursor.fetchall()

        col_names = [desc[0] for desc in cursor.description]
        # lista de dicionários com nomes de campos e valores
        formatted_results = []
        for row in results:
            formatted_result = {}
            for i, col_name in enumerate(col_names):
                formatted_result[col_name] = row[i]
            formatted_results.append(formatted_result)

        return formatted_results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_select_livro_premiacao(): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # consulta na tabela livro_premiacao
        cursor.execute("SELECT * FROM lib.livro_premiacao")
        results = cursor.fetchall()

        return results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()