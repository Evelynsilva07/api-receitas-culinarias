from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models.ingrediente import IngredienteModel
from models.receita import ReceitaModel
from schemas.ingrediente import IngredienteSchema, IngredienteUpdateSchema

ingrediente_blp = Blueprint("Ingredientes", __name__, description="Operações com ingredientes")

@ingrediente_blp.route("/ingredientes")
class IngredienteList(MethodView):

    @ingrediente_blp.response(200, IngredienteSchema(many=True))
    def get(self):
        return IngredienteModel.query.all()

    @ingrediente_blp.arguments(IngredienteSchema)
    @ingrediente_blp.response(201, IngredienteSchema)
    def post(self, data):
        if not ReceitaModel.query.get(data["receita_id"]):
            abort(404, message="Receita não encontrada")

        ingrediente = IngredienteModel(**data)
        db.session.add(ingrediente)
        db.session.commit()
        return ingrediente
