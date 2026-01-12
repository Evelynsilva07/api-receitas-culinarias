from flask.views import MethodView
from flask_smorest import Blueprint, abort
import uuid

from db import receitas
from schemas.receita import ReceitaSchema, ReceitaSchemaUpdate

receita_blp = Blueprint(
    "Receitas",
    __name__,
    description="Operações relacionadas a receitas culinárias"
)

@receita_blp.route("/receitas")
class ReceitaList(MethodView):

    @receita_blp.response(200, ReceitaSchema(many=True))
    def get(self):
        return receitas.values()

    @receita_blp.arguments(ReceitaSchema)
    @receita_blp.response(201, ReceitaSchema)
    def post(self, dados):
        receita_id = uuid.uuid4().hex
        nova_receita = {**dados, "id": receita_id}
        receitas[receita_id] = nova_receita
        return nova_receita


@receita_blp.route("/receitas/<string:receita_id>")
class ReceitaId(MethodView):

    @receita_blp.response(200, ReceitaSchema)
    def get(self, receita_id):
        if receita_id not in receitas:
            abort(404, message="Receita não encontrada")
        return receitas[receita_id]

    @receita_blp.arguments(ReceitaSchema)
    @receita_blp.response(200, ReceitaSchema)
    def put(self, dados, receita_id):
        if receita_id not in receitas:
            abort(404, message="Receita não encontrada")

        if "id" in dados and dados["id"] != receita_id:
            abort(400, message="Não é permitido alterar o id")

        receitas[receita_id].update(dados)
        return receitas[receita_id]

    @receita_blp.arguments(ReceitaSchemaUpdate)
    @receita_blp.response(200, ReceitaSchema)
    def patch(self, dados, receita_id):
        if receita_id not in receitas:
            abort(404, message="Receita não encontrada")

        if not dados:
            abort(400, message="Nenhum campo enviado para atualização")

        receitas[receita_id].update(dados)
        return receitas[receita_id]

    @receita_blp.response(200)
    def delete(self, receita_id):
        if receita_id not in receitas:
            abort(404, message="Receita não encontrada")

        receitas.pop(receita_id)
        return {"message": "Receita removida com sucesso"}
