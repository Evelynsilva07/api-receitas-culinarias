from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models.receita import ReceitaModel
from schemas.receita import ReceitaSchema, ReceitaUpdateSchema

receita_blp = Blueprint("Receitas", __name__, description="Operações com receitas")

@receita_blp.route("/receitas")
class ReceitaList(MethodView):

    @receita_blp.response(200, ReceitaSchema(many=True))
    def get(self):
        return ReceitaModel.query.all()

    @receita_blp.arguments(ReceitaSchema)
    @receita_blp.response(201, ReceitaSchema)
    def post(self, data):
        receita = ReceitaModel(**data)
        db.session.add(receita)
        db.session.commit()
        return receita
