from marshmallow import fields, Schema


class DemoSchema(Schema):
	question = fields.String(required=True, description="Please enter your question")
	file = fields.Raw(required=False, description="Upload a PDF file")