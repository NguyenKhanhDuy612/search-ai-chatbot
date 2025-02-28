from marshmallow import fields, Schema


class DemoSchema(Schema):
	question = fields.String(required=True)
