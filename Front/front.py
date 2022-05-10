from flask import Flask, render_template, request
import main.py


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/<string:nome>')
def error(nome):
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError2=MsgError)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
