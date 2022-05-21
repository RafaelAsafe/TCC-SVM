import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_bootstrap import Bootstrap


DIRETORIO = "C:\\Users\\Mysterio\\OneDrive - ifsp.edu.br\\Documentos\\Asafe IFSP\\TCC\\programação\\APis\\TESTE_API_ARQUIVOS"


app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html",**locals())# rederizar paginas html -**locals() passa todas as variaveis do app pro template má pratica usar somente no dev!!!!!!


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/<string:nome>')
def error(nome):
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError2=MsgError)


@app.route("/arquivos", methods=["POST"])
def post_arquivo():
    arquivo = request.files.get("meuArquivo")

    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))

    return 'Arquivo Recebido com sucesso', 201


if __name__ == "__main__":
    app.run(debug=True, port=8000)
