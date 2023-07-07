from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root@localhost/flask_react_crud"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "email", "data")


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


@app.route("/")
def hello_world():
    return "<p>Olá, Mundo!</p>"


@app.route("/listadeusuarios", methods=["GET"])
def listadeusuarios():
    all_usuarios = Usuario.query.all()
    results = usuarios_schema.dump(all_usuarios)
    return jsonify(results)


@app.route("/usuarioadd", methods=["POST"])
def usuarioadd():
    nome = request.json["nome"]
    email = request.json["email"]

    usuario = Usuario(nome, email)
    db.session.add(usuario)
    db.session.commit()

    return usuario_schema.jsonify(usuario)


if __name__ == "__main__":
    app.run()
