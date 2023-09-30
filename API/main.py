from flask import Flask, request, jsonify
from connectbd import bd_config
from id_check import id_livro_exists, id_autor_exists, id_livro_premiacao_exists
from selects import exec_select_livro, exec_select_autor, exec_select_livro_premiacao
from deletes import exec_delete_livro, exec_delete_autor, exec_delete_livro_premiacao
from inserts import exec_insert_autor #, exec_insert_livro, exec_insert_autor_premiacao
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

@app.route('/delete/livro/<int:id_livro>', methods=['DELETE'])  # para deletar um livro pelo seu ID
def delete_from_table_livro(id_livro):
    if not id_livro_exists(id_livro):
        return jsonify({"error": "ID do livro nao encontrado na tabela."}), 404
    
    if exec_delete_livro(id_livro):
        return jsonify({"status": f"Exclusao do registro {id_livro} bem-sucedida."})
    else:
        return jsonify({"error": f"Erro ao excluir o registro {id_livro}."})
    
@app.route('/delete/autor/<int:id_autor>', methods=['DELETE'])  # para deletar um autor pelo seu ID
def delete_from_table_autor(id_autor):
    if not id_autor_exists(id_autor):
        return jsonify({"error": "ID do autor nao encontrado na tabela."}), 404
    
    if exec_delete_autor(id_autor):
        return jsonify({"status": f"Exclusao do registro {id_autor} bem-sucedida."})
    else:
        return jsonify({"error": f"Erro ao excluir o registro {id_autor}."})

@app.route('/delete/livropremiacao', methods=['DELETE'])
def delete_from_table_livro_premiacao():
    try:
        data = request.get_json()

        id_livro = data.get('id_livro')
        id_premiacao = data.get('id_premiacao')

        if id_livro is None or id_premiacao is None:
            return jsonify({"error": "Forneça os IDs 'id_livro' e 'id_premiacao' no corpo da solicitação."}), 400

        if not id_livro_premiacao_exists(id_livro, id_premiacao):
            return jsonify({"error": "Esses IDs nao possuem uma relacao na tabela."}), 404
    
        if exec_delete_livro_premiacao(id_livro, id_premiacao):
            return jsonify({"status": f"Exclusao dos registros {id_livro} e {id_premiacao} bem-sucedida."})
        else:
            return jsonify({"error": f"Erro ao excluir o registro {id_livro} e {id_premiacao}."})
    except Exception as e: return jsonify({"error": str(e)}), 400

# OPERAÇÕES DE INSERT

@app.route('/insert/autor', methods=['POST'])
def insert_autor():
    try:
        data = request.get_json()

        id_autor = data.get('id_autor')
        p_nome = data.get('primeiro_nome')
        sobrenome = data.get('sobrenome')
        nacionalidade = data.get('nacionalidade')

        if id_autor is None or p_nome is None or sobrenome is None or nacionalidade is None:
            return jsonify({"error": "Forneça os dados do autor no corpo da solicitação (id_autor, primeiro_nome, sobrenome e nacionalidade)."}), 400
    
        if exec_insert_autor(id_autor, p_nome, sobrenome, nacionalidade):
            return jsonify({"status": "Inserção do autor bem-sucedida."})
        else:
            return jsonify({"error": "Erro ao inserir o autor."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)