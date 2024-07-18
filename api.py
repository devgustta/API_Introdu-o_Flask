from flask import Flask, jsonify, request

app = Flask(__name__)

ceps = [
    {
        "cep": 87780000,
        "nome": "Paraiso do Norte",
        "bairro": "Centro",
        "uf": "PR"
    },

    {
        "cep": 87704100,
        "nome": "Paranavai",
        "bairro": "Centro",
        "uf": "PR"
    },

    {
        "cep": 87200-000,
        "nome": "Cianorte",
        "bairro": "Centro",
        "uf": "PR"
    }

]

@app.route('/cep',methods=['GET'])
def retornar_ceps():
    return jsonify(ceps)

@app.route('/cep/<int:consulta>', methods=['GET'])
def consultar_cep(consulta):
    for cep in ceps:
        if cep.get("cep") == consulta:
            return jsonify(cep)

@app.route('/cep/<int:consulta>', methods=['PUT'])
def editar_cep(consulta):
    cep_alterado = request.get_json()
    for indice, cep in enumerate(ceps):
        if cep.get('cep') == consulta:
            ceps[indice].update(cep_alterado)
            return jsonify(ceps[indice])




app.run(debug=True)