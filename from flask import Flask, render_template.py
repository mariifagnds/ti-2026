from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'chave_secreta_para_desenvolvimento_seguro'

@app.route('/')
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    if 'tarefas' not in session:
        session['tarefas'] = []
        
    return render_template('index.html', usuario=session['usuario'], tarefas=session['tarefas'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
       
        if usuario and senha == '1234':
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro="Credenciais inválidas. Tente a senha '1234'.")
            
    return render_template('login.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    if 'usuario' not in session:
        return redirect(url_for('login'))
        
    nova_tarefa = request.form.get('tarefa')
    if nova_tarefa:
        tarefas = session.get('tarefas', [])
        tarefas.append(nova_tarefa)
        session['tarefas'] = tarefas
        
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('tarefas', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)