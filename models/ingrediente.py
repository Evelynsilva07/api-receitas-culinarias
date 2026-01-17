from db import db

class IngredienteModel(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.String(50), nullable=False)

    receita_id = db.Column(
        db.Integer,
        db.ForeignKey("receitas.id", ondelete="CASCADE"),
        nullable=False
    )

    receita = db.relationship("ReceitaModel", back_populates="ingredientes")
