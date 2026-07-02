from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = "categoria"

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(10), nullable=False)

    itens = db.relationship(
        "Item",
        backref="categoria",
        lazy=True,
        cascade="all, delete"
    )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "sigla": self.sigla
        }

class Item(db.Model):
    __tablename__ = "item"

    patrimonio = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(10, 2))
    responsavel_email = db.Column(db.String(150))
    localizacao = db.Column(db.String(200))

    codigo_cat = db.Column(
        db.Integer,
        db.ForeignKey("categoria.codigo"),
        nullable=False
    )

    def to_dict(self):
        return {
            "patrimonio": self.patrimonio,
            "nome": self.nome,
            "valor": float(self.valor) if self.valor else None,
            "responsavel_email": self.responsavel_email,
            "localizacao": self.localizacao,
            "codigo_cat": self.codigo_cat,
            "categoria": self.categoria.nome if self.categoria else None
        }
