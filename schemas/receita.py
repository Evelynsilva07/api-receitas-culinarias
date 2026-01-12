from marshmallow import Schema, fields

class ReceitaSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    ingredientes = fields.List(fields.Str(), required=True)
    modo_preparo = fields.Str(required=True)

class ReceitaSchemaUpdate(Schema):
    nome = fields.Str(required=False)
    ingredientes = fields.List(fields.Str(), required=False)
    modo_preparo = fields.Str(required=False)
