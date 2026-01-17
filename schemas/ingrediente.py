from marshmallow import Schema, fields
from schemas.plain import PlainIngredienteSchema

class IngredienteSchema(PlainIngredienteSchema):
    receita_id = fields.Int(required=True)

class IngredienteUpdateSchema(Schema):
    nome = fields.Str(required=False)
    quantidade = fields.Str(required=False)
    receita_id = fields.Int(required=False)
