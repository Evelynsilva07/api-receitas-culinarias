from marshmallow import Schema, fields

class PlainReceitaSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    descricao = fields.Str()

class PlainIngredienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    quantidade = fields.Str(required=True)
