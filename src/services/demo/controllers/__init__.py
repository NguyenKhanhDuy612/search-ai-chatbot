from flask import Response
from flask_apispec import doc, marshal_with, MethodResource, use_kwargs
from flask_restful import Resource

from src.services.demo.models.demo_schema import DemoSchema
from src.services.demo.services import DemoService
from langchain_community.document_loaders import PyMuPDFLoader

@doc(tags=["Demo"])
class DemoControllerAPI(MethodResource, Resource):

	@doc(description="Answer question using Gemini API")
	@use_kwargs(DemoSchema, location="query")
	@marshal_with(DemoSchema, code=200, description="Success")
	def get(self, question: str):
		response = DemoService.ask_question(question)

		return Response(response, mimetype='text/plain')


class PDFLoaderControllerAPI(MethodResource, Resource):
	@doc(description="Load PDF and return content", tags=["PDF"])
	@marshal_with(DemoSchema, code=200, description="Success")
	def get(self):
		try:
			# Đường dẫn tới file PDF
			file_path = "D:/canhan/Documentation.pdf"

			# Tạo loader
			loader = PyMuPDFLoader(file_path)

			# Load PDF 
			docs = loader.load()

			# Tổng hợp toàn bộ nội dung PDF
			full_pdf_content = ""
			for doc in docs:
				full_pdf_content += f"--- Page {doc.metadata.get('page', 'N/A')} ---\n"
				full_pdf_content += doc.page_content + "\n\n"

			# Trả về response plain text
			return Response(full_pdf_content, mimetype='text/plain')


		except Exception as e:
			return jsonify({
				"error": str(e),
				"message": "Failed to load PDF"
			}), 500

	# @doc(description="Load specific page of PDF", tags=["PDF"])
	# def get_page(self, page_number: int):
	# 	try:
	# 		# Đường dẫn tới file PDF
	# 		file_path = "D:/canhan/Documentation.pdf"

	# 		# Tạo loader
	# 		loader = PyMuPDFLoader(file_path)

	# 		# Load PDF 
	# 		docs = loader.load()

	# 		# Kiểm tra số trang hợp lệ
	# 		if page_number < 0 or page_number >= len(docs):
	# 			return Response(
	# 				f"Invalid page number. Must be between 0 and {len(docs) - 1}", 
	# 				status=400, 
	# 				mimetype='text/plain'
	# 			)

	# 		# Lấy trang cụ thể
	# 		page_doc = docs[page_number]

	# 		# Trả về nội dung trang dưới dạng plain text
	# 		page_content = (
	# 			f"--- Page {page_doc.metadata.get('page', page_number)} ---\n"
	# 			f"Source: {page_doc.metadata.get('source', '')}\n"
	# 			f"Creator: {page_doc.metadata.get('creator', '')}\n"
	# 			f"Producer: {page_doc.metadata.get('producer', '')}\n"
	# 			f"Creation Date: {page_doc.metadata.get('creationdate', '')}\n\n"
	# 			f"{page_doc.page_content}"
	# 		)

	# 		return Response(page_content, mimetype='text/plain')

	# 	except Exception as e:
	# 		return Response(
	# 			f"Error loading PDF page: {str(e)}", 
	# 			status=500, 
	# 			mimetype='text/plain'
	# 		)

