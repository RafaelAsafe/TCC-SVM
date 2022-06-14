import os
from flask import abort, render_template, request
from vitreus.models import Patient


def index():
    return render_template("index.html")

def sobre():
    return render_template('sobre.html')

def error(nome):
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError=MsgError)

def patients():
    patients = Patient.query.all()
    return render_template("patients.html", patients=patients)

def patient(patient_id):
    patient = Patient.query.filter_by(id=patient_id).first() or abort(
        404, "Paciente nao encontrado"
    )
    return render_template("patient.html", patient=patient)


def post_arquivo():
    DIRETORIO = "C:\\Users\\Mysterio\\OneDrive - ifsp.edu.br\\Documentos\\Asafe IFSP\\TCC\\programação\\APis\\TESTE_API_ARQUIVOS"
    arquivo = request.files.get("meuArquivo")
    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))
    return 'Arquivo Recebido com sucesso', 201


