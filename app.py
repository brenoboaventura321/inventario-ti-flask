from flask import Flask, render_template
from config import Config
from models import db, Categoria, Item

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/categorias")
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template("categorias.html", categorias=categorias)

@app.route("/itens")
def listar_itens():
    itens = Item.query.all()
    return render_template("itens.html", itens=itens)

@app.route("/relatorio-itens")
def relatorio_itens():
    itens = Item.query.all()
    resultado = []
    for item in itens:
        resultado.append({
            "patrimonio": item.patrimonio,
            "nome": item.nome,
            "valor": float(item.valor) if item.valor else None,
            "responsavel_email": item.responsavel_email,
            "localizacao": item.localizacao,
            "categoria": item.categoria.nome,
            "sigla_categoria": item.categoria.sigla
        })
    return resultado

@app.route("/relatorio-categorias")
def relatorio_categorias():
    categorias = Categoria.query.all()
    resultado = []
    for categoria in categorias:
        resultado.append({
            "codigo": categoria.codigo,
            "nome": categoria.nome,
            "sigla": categoria.sigla,
            "total_itens": len(categoria.itens)
        })
    return resultado

if __name__ == "__main__":
    app.run(debug=True)
