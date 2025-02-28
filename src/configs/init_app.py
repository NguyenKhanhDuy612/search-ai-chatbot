from flask import Flask

from src.configs.extensions import api, docs
from src.configs.flask_config import DefaultConfig
from src.configs.urls import all_apis


def init_routes(app):
	for url in all_apis:
		api.add_resource(url.resource, url.url, endpoint=url.url)
		app.add_url_rule(
			url.url,
			endpoint=url.url,
			view_func=url.resource.as_view(url.url[1:]),
		)
		docs.register(url.resource, endpoint=url.url)


def create_app(config_class=DefaultConfig):
	app = Flask(__name__)

	app.config.from_object(config_class)
	api.init_app(app)
	init_routes(app)
	docs.init_app(app)

	return app
