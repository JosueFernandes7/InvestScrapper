from flask import Flask, render_template, request, jsonify
from scrapper import buscaDados
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="start")

@app.route('/enviar', methods=['POST'])
def enviar():
    # Obtém os dados enviados no corpo da requisição POST
    tipo = request.form.get('tipo')
    valor = request.form.get('valor')
    nome = request.form.get('nome')

    # Realiza alguma lógica com os dados
    print(tipo,nome,valor)
    data = buscaDados(str(tipo),str(nome),float(valor))
    print(data)
    dataAtual = datetime.now().strftime("%d/%m/%Y")
    # Retorna uma resposta em formato JSON
    return render_template('final.html', total=data["total"],valorInvestido=data["valor_Investido"],mod=data["mod"],valorizacao=data["valorizacao"],dataAtual=str(dataAtual),nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
