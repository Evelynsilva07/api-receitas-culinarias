from marshmallow import Schema, fields
from schemas.plain import PlainReceitaSchema, PlainIngredienteSchema

class ReceitaSchema(PlainReceitaSchema):
    ingredientes = fields.List(
        fields.Nested(PlainIngredienteSchema()),
        dump_only=True
    )

class ReceitaUpdateSchema(Schema):
    nome = fields.Str(required=False)
    descricao = fields.Str(required=False)
