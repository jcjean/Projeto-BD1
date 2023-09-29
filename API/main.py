from flask import Flask, request, jsonify
from connectbd import bd_config
from selects import exec_select_livro, exec_select_autor, exec_select_livro_premiacao
from deletes import exec_delete_livro #id_exists, exec_delete_autor, exec_delete_livro_premiacao
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

# OPERAÇÕES DE CONSULTA
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
    
@app.route('/select/livropremiacao')     # para rodar o select na tabela de relacionamento livro_premiacao
def select_from_table_livro_premiacao():
    results = exec_select_livro_premiacao()
    if results is not None:
        return jsonify({"Livros e Premiacoes": results})
    else:
        return jsonify({"error": "Erro ao executar a consulta."})
    
# OPERAÇÕES DE DELETE
@app.route('/delete/livro/<int:id_livro>', methods=['DELETE'])
def delete_from_table_livro(id_livro):
    #if not id_exists(id_livro):
    #    return jsonify({"error": "ID não encontrado na tabela."}), 404
    
    if exec_delete_livro(id_livro):
        return jsonify({"status": f"Exclusao do registro {id_livro} bem-sucedida."})
    else:
        return jsonify({"error": f"Erro ao excluir o registro {id_livro}."})

if __name__ == '__main__':
    app.run(debug=True)