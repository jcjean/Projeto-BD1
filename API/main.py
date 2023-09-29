from flask import Flask, jsonify
from connectbd import bd_config
from selects import exec_select_livro, exec_select_autor, exec_select_livro_premiacao
#from inserts import exec_insert_livro, exec_insert_autor, exec_insert_autor_premiacao
import psycopg2

app = Flask(__name__)

def test_database_connection():
    try:
        conn = psycopg2.connect(**bd_config)
        return True
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return False
    finally:
        if 'conn' in locals():
            conn.close()

@app.route('/select/livro')     # para rodar o select na tabela livro
def select_from_table_livro():
    results = exec_select_livro()
    if results is not None:
        return jsonify({"Livros": results})
    else:
        return jsonify({"error": "Erro ao executar a consulta."})
    
@app.route('/select/autor')     # para rodar o select na tabela autor
def select_from_table_autor():
    results = exec_select_autor()
    if results is not None:
        return jsonify({"Autores": results})
    else:
        return jsonify({"error": "Erro ao executar a consulta."})
    
@app.route('/select/livropremiacao')     # para rodar o select na tabela livro_premiacao
def select_from_table_livro_premiacao():
    results = exec_select_livro_premiacao()
    if results is not None:
        return jsonify({"Livros e Premiacoes": results})
    else:
        return jsonify({"error": "Erro ao executar a consulta."})

if __name__ == '__main__':
    app.run(debug=True)