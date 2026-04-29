from flask import Flask, request, jsonify
import pdfplumber

app = Flask(__name__)

@app.route("/")
def home():
    return "PDF Timetable API Running!"

@app.route("/pdf", methods=["POST"])
def pdf():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    try:
        text_all = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
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
            "error": str(e)
        })
