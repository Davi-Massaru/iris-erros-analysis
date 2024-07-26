from flask import Flask, render_template
import pandas as pd
import LoadErrors

app = Flask(__name__)

@app.route('/')
def index():
    LoadErrors.charge()
    return render_template('index.html')

@app.route('/charge')
def charge():
    LoadErrors.charge()
    return "Erro carregado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
