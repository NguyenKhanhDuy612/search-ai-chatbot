from flask import Response
from flask_apispec import doc, marshal_with, MethodResource, use_kwargs
from flask_restful import Resource

from src.services.demo.models.demo_schema import DemoSchema
from src.services.demo.services import DemoService


@doc(tags=["Demo"])
class DemoControllerAPI(MethodResource, Resource):

	@doc(description="Answer question using Gemini API")
	@use_kwargs(DemoSchema, location="query")
	@marshal_with(DemoSchema, code=200, description="Success")
	def get(self, question: str):
		response = DemoService.ask_question(question)

		return Response(response, mimetype='text/plain')
