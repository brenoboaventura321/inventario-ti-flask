from flask import Flask, render_template, request, redirect

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

@app.route("/editar-item/<int:patrimonio>", methods=["GET", "POST"])
def editar_item(patrimonio):
    item = Item.query.get_or_404(patrimonio)
    categorias = Categoria.query.all()
    
    if request.method == "POST":
        item.nome = request.form["nome"]
        item.valor = float(request.form["valor"]) if request.form["valor"] else None
        item.responsavel_email = request.form["responsavel_email"]
        item.localizacao = request.form["localizacao"]
        item.codigo_cat = int(request.form["codigo_cat"])
        db.session.commit()
        
        return redirect("/itens")
        
    return render_template("editar_item.html", item=item, categorias=categorias)

@app.route("/novo-item", methods=["GET", "POST"])
def novo_item():
    categorias = Categoria.query.all()
    
    if request.method == "POST":
        patrimonio = int(request.form["patrimonio"])
        nome = request.form["nome"]
        valor = float(request.form["valor"]) if request.form["valor"] else None
        responsavel_email = request.form["responsavel_email"]
        localizacao = request.form["localizacao"]
        codigo_cat = int(request.form["codigo_cat"])
        
        item_novo = Item(
            patrimonio=patrimonio,
            nome=nome,
            valor=valor,
            responsavel_email=responsavel_email,
            localizacao=localizacao,
            codigo_cat=codigo_cat
        )
        
        db.session.add(item_novo)
        db.session.commit()
        
        return redirect("/itens")
        
    return render_template("novo_item.html", categorias=categorias)

@app.route("/deletar-item/<int:patrimonio>", methods=["GET", "POST"])
def deletar_item(patrimonio):
    item = Item.query.get_or_404(patrimonio)
    
    db.session.delete(item)
    db.session.commit()
    
    return redirect("/itens")
