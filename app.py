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
                text_all += page.extract_text() + "\n"

        # とりあえずテキスト返す（後で時間割に変換する）
        return jsonify({
            "success": True,
            "text": text_all[:2000]  # 長すぎ防止
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })
