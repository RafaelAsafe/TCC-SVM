import os
from flask import abort, render_template, request


def index():
    return render_template("index.html")

def sobre():
    return render_template('sobre.html')

def error(nome):
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError=MsgError)

def post_arquivo():
    DIRETORIO = "C:\\Users\\Mysterio\\OneDrive - ifsp.edu.br\\Documentos\\Asafe IFSP\\TCC\\programação\\APis\\TESTE_API_ARQUIVOS"
    arquivo = request.files.get("meuArquivo")
    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))
    return 'Arquivo Recebido com sucesso', 201


