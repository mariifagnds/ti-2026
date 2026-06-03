from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cadastro():

    erros = []
    sucesso = None

    if request.method == "POST":

        nome = request.form.get("nome", "").strip().title()
        email = request.form.get("email", "").strip().lower()
        telefone = request.form.get("telefone", "").strip()
        cpf = request.form.get("cpf", "").strip()
        cidade = request.form.get("cidade", "").strip().title()
        estado = request.form.get("estado", "").strip().upper()
        curso = request.form.get("curso", "").strip()
        idade = request.form.get("idade", "").strip()
        senha = request.form.get("senha", "").strip()

        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace(" ", "")

        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")

        if not all([nome, email, telefone, cpf, cidade, estado, curso, idade, senha]):
            erros.append("Preencha todos os campos obrigatórios.")

        if len(nome) < 8:
            erros.append("Nome inválido.")

        if "@" not in email or ".com" not in email:
            erros.append("E-mail inválido.")

        if not telefone.isdigit() or len(telefone) != 11:
            erros.append("Telefone inválido.")

        if not cpf.isdigit() or len(cpf) != 11:
            erros.append("CPF inválido.")

        if len(cidade) < 3:
            erros.append("Cidade inválida.")

        if len(estado) != 2 or not estado.isalpha():
            erros.append("Estado inválido.")

        if curso == "":
            erros.append("Curso inválido.")

        if not idade.isdigit():
            erros.append("Idade inválida.")
        else:
            if int(idade) < 16:
                erros.append("Idade mínima é 16 anos.")

        possui_numero = any(caractere.isdigit() for caractere in senha)

        if len(senha) < 8 or not possui_numero:
            erros.append("Senha muito fraca.")

        if not erros:
            sucesso = {
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "cpf": cpf,
                "cidade": cidade,
                "estado": estado,
                "curso": curso,
                "idade": idade
            }

    return render_template(
        "index.html",
        erros=erros,
        sucesso=sucesso
    )

if __name__ == "__main__":
    app.run(debug=True)