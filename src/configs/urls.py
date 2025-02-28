from src.services.demo.controllers import DemoControllerAPI
from src.services.demo.controllers import PDFLoaderControllerAPI


class API:
	def __init__(self, resource, url):
		self.resource = resource
		self.url = url


all_apis = [
	API(DemoControllerAPI, "/demo"),
	API(PDFLoaderControllerAPI, "/demo1"),
]
