from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função auxiliar para conectar no banco de dados SQLite
def conectar_banco():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row # Permite acessar colunas pelo nome
    return conexao

# Rota Principal (Lista os cadastros usando SELECT / JOIN)
@app.route('/')
def index():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    # Exemplo de consulta parecida com a questão 12
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conexao.close()
    return render_template('index.html', produtos=produtos)

# Rota de Cadastro (Aceita GET para mostrar o form e POST para receber os dados)
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Captura o dado enviado pelo formulário (questão 10)
        nome_produto = request.form['nome']
        
        # Salvando no SQLite
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO produtos (nome) VALUES (?)', (nome_produto,))
        conexao.commit()
        conexao.close()
        
        return redirect(url_for('index'))
        
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)