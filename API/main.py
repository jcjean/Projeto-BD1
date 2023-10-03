from flask import Flask, request, jsonify
from connectbd import bd_config
from id_check import id_livro_exists, id_autor_exists, id_livro_premiacao_exists
from selects import exec_select_livro, exec_select_autor, exec_select_livro_premiacao
from deletes import exec_delete_livro, exec_delete_autor, exec_delete_livro_premiacao
from inserts import exec_insert_autor, exec_insert_livro, exec_insert_livro_premiacao
from updates import exec_update_livro, exec_update_autor, exec_update_livro_premiacao
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

@app.route('/select/livro')    # para rodar o select na tabela livro
def select_from_table_livro():
    try:
        data = request.get_json()

        results = exec_select_livro(data)
        if results is not None:
            return jsonify(results)
        else:
            return jsonify({"error": "Erro ao executar a consulta."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/select/autor')     # para rodar o select na tabela autor
def select_from_table_autor():
    try:
        data = request.get_json()

        results = exec_select_autor(data)
        if results is not None:
            return jsonify(results)
        else:
            return jsonify({"error": "Erro ao executar a consulta."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/select/livropremiacao')     # para rodar o select na tabela de relacionamento livro_premiacao
def select_from_table_livro_premiacao():
    try:
        data = request.get_json()

        results = exec_select_livro_premiacao(data)
        if results is not None:
            return jsonify({"Livros e Premiacoes": results})
        else:
            return jsonify({"error": "Erro ao executar a consulta."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# OPERAÇÕES DE DELETE

@app.route('/delete/livro/<int:id_livro>', methods=['DELETE'])  # para deletar um livro pelo seu ID
def delete_from_table_livro(id_livro):
    if not id_livro_exists(id_livro):
        return jsonify({"error": "ID do livro nao encontrado na tabela."}), 404
    
    if exec_delete_livro(id_livro):
        return jsonify({"status": f"Exclusao do livro {id_livro} bem-sucedida."})
    else:
        return jsonify({"error": f"Erro ao excluir o livro {id_livro}."})
    
@app.route('/delete/autor/<int:id_autor>', methods=['DELETE'])  # para deletar um autor pelo seu ID
def delete_from_table_autor(id_autor):
    if not id_autor_exists(id_autor):
        return jsonify({"error": "ID do autor nao encontrado na tabela."}), 404
    
    if exec_delete_autor(id_autor):
        return jsonify({"status": f"Exclusao do autor {id_autor} bem-sucedida."})
    else:
        return jsonify({"error": f"Erro ao excluir o autor {id_autor}."})

@app.route('/delete/livropremiacao', methods=['DELETE'])    # para deletar da tabela livro_premiacao pelo seu ID
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

@app.route('/insert/autor', methods=['POST'])   # para inserir um autor na tabela
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
            return jsonify({"status": f"Inserção do autor {p_nome}{sobrenome} bem-sucedida."})
        else:
            return jsonify({"error": "Erro ao inserir o autor."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/insert/livro', methods=['POST'])   # para inserir um livro na tabela
def insert_livro():
    try:
        data = request.get_json()

        id_livro = data.get('id_livro')
        isbn = data.get('isbn')
        titulo = data.get('titulo')
        ano_pub = data.get('ano_publicacao')
        sinopse = data.get('sinopse')
        id_autor = data.get('id_autor')
        id_editora = data.get('id_editora')

        if id_livro is None or isbn is None or titulo is None or ano_pub is None or sinopse is None or id_autor is None or id_editora is None:
            return jsonify({"error": "Forneça os dados do livro no corpo da solicitação (id_livro, isbn, titulo, sinopse, id_autor e id_editora)."}), 400
    
        if exec_insert_livro(id_livro, isbn, titulo, ano_pub, sinopse, id_autor, id_editora):
            return jsonify({"status": f"Inserção do livro {titulo} bem-sucedida."})
        else:
            return jsonify({"error": "Erro ao inserir o livro."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/insert/livropremiado', methods=['POST'])   # para inserir um livro e seu premio na tabela livro_premiacao
def insert_livro_premiacao():
    try:
        data = request.get_json()

        id_livro = data.get('id_livro')
        id_premiacao = data.get('id_premiacao')
        data_premiacao = data.get('data_premiacao')

        if id_livro is None or id_premiacao is None or data_premiacao is None:
            return jsonify({"error": "Forneça os dados do livro premiado no corpo da solicitação (id_livro, id_premiacao e data_premiacao)."}), 400
        
        if exec_insert_livro_premiacao(id_livro, id_premiacao, data_premiacao):
            return jsonify({"status": "Inserção do livro e sua premiação bem-sucedida."})
        else:
            return jsonify({"error": "Erro ao inserir as informações."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# OPERAÇÕES DE UPDATE

@app.route('/update/livro/<int:id_livro>', methods=['PUT'])     # para atualizar o dado de um livro na tabela
def update_livro(id_livro):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Forneça os campos a serem atualizados no corpo da solicitação: id_livro, isbn, titulo, sinopse, id_autor e/ou id_editora."}), 400
        
        if not id_livro_exists(id_livro):
            return jsonify({"error": "ID do livro nao encontrado na tabela."}), 404
        
        if exec_update_livro(id_livro, data):
            return jsonify({"status": f"Atualização do livro {id_livro} bem-sucedida."})
        else:
            return jsonify({"error": f"Erro ao atualizar o livro {id_livro}."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/update/autor/<int:id_autor>', methods=['PUT'])     # para atualizar o dado de um autor na tabela
def update_autor(id_autor):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Forneça os campos a serem atualizados no corpo da solicitação: id_autor, primeiro_nome, sobrenome e/ou nacionalidade."}), 400
        
        if not id_autor_exists(id_autor):
            return jsonify({"error": "ID do autor nao encontrado na tabela."}), 404

        if exec_update_autor(id_autor, data):
            return jsonify({"status": f"Atualização do autor {id_autor} bem-sucedida."})
        else:
            return jsonify({"error": f"Erro ao atualizar o autor {id_autor}."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/update/livropremiacao/<int:id_livro>/<int:id_premiacao>', methods=['PUT'])     # para atualizar o dado de um livro premiado na tabela livro_premiacao
def update_livro_premiacao(id_livro, id_premiacao):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Forneça os campos a serem atualizados no corpo da solicitação: id_livro, id_premiacao e/ou data_premiacao"}), 400
        
        if not id_livro_premiacao_exists(id_livro, id_premiacao):
            return jsonify({"error": "Esses IDs nao possuem uma relacao na tabela."}), 404

        if exec_update_livro_premiacao(id_livro, id_premiacao, data):
            return jsonify({"status": f"Atualização da relação livro-premiacao bem-sucedida para livro {id_livro} e premiação {id_premiacao}."})
        else:
            return jsonify({"error": f"Erro ao atualizar o livro."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400 

if __name__ == '__main__':
    app.run(debug=True)