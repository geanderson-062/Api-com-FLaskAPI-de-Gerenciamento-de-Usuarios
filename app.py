from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime

# run api flask --app hello run
# no lugar do hello colocar o nome do arquivo

app = Flask(__name__)

# Configura o banco de dados SQLite em relação à pasta de instância do aplicativo.
# Substitua "root" pelo nome de usuário real e "flask_react_crud" pelo nome real do banco de dados.
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root@localhost/flask_react_crud"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


@app.route("/")
def hello_world():
    return "<p>Olá, Mundo!</p>"


@app.route("/usuarioadd", methods=["POST"])
def usuarioadd():
    nome = request.json["nome"]
    email = request.json["email"]

    usuario = Usuario(nome, email)
    db.session.add(usuario)
    db.session.commit()

    return jsonify({"sucesso": "Postagem realizada com sucesso"})


if __name__ == "__main__":
    app.run()
