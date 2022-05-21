from flask import abort, render_template

def index():
    return render_template("index.html")

def sobre():
    return render_template('sobre.html')

def error():
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError=MsgError)

def post_arquivo():
    arquivo = request.files.get("meuArquivo")
    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))
    return 'Arquivo Recebido com sucesso', 201


