from flask import Flask, request, jsonify
import pdfplumber
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return "PDF Timetable API Running!"

@app.route("/pdf", methods=["POST"])
def pdf():
    try:
        if "file" not in request.files:
            return jsonify({
                "success": False,
                "error": "No file uploaded"
            }), 400

        file = request.files["file"]

        text_all = ""

        with pdfplumber.open(file.stream) as pdf:
            for i, page in enumerate(pdf.pages):
                if i >= 18:
                    break

                text = page.extract_text()
                if text:
                    text_all += text + "\n"

        return jsonify({
            "success": True,
            "text": text_all
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }), 200
