from db import db

class ReceitaModel(db.Model):
    __tablename__ = "receitas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))

    ingredientes = db.relationship(
        "IngredienteModel",
        back_populates="receita",
        cascade="all, delete-orphan"
    )
