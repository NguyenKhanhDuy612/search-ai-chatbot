from flask import Flask, Response, jsonify
from flask_restful import Api, Resource
import fitz  # PyMuPDF
import pdfplumber

app = Flask(__name__)
api = Api(app)

PDF_PATH = r"D:\canhan\Documentation.pdf"  # Đường dẫn file PDF


class PDFReaderAPI(Resource):
    def get(self):
        """ Đọc nội dung từ file PDF và trả về dưới dạng text """
        try:
            text = self.extract_text_pymupdf(PDF_PATH)
            return Response(text, mimetype='text/plain')
        except Exception as e:
            return jsonify({"error": str(e)})

    @staticmethod
    def extract_text_pymupdf(pdf_path: str) -> str:
        """ Đọc nội dung PDF bằng PyMuPDF """
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        return text

    # @staticmethod
    # def extract_text_pdfplumber(pdf_path: str) -> str:
    #     """ Đọc nội dung PDF bằng pdfplumber """
    #     text = ""
    #     with pdfplumber.open(pdf_path) as pdf:
    #         for page in pdf.pages:
    #             text += page.extract_text() + "\n"
    #     return text


# Đăng ký API
api.add_resource(PDFReaderAPI, "/read-pdf")

if __name__ == "__main__":
    app.run(debug=True)
