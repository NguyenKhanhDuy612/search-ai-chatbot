from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from src.configs.settings import flask_debug


class DefaultConfig:
	DEBUG = flask_debug
	TESTING = False

	# Swagger stuff
	APISPEC_SWAGGER_URL = "/api/"
	APISPEC_SWAGGER_UI_URL = "/"
	APISPEC_SPEC = APISpec(
		title="Research AI Chatbot",
		version="v1",
		openapi_version="2.0.0",
		plugins=[MarshmallowPlugin()]
	)
