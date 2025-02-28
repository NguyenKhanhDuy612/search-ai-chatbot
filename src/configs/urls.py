from src.services.demo.controllers import DemoControllerAPI


class API:
	def __init__(self, resource, url):
		self.resource = resource
		self.url = url


all_apis = [
	API(DemoControllerAPI, "/demo"),
]
