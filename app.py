from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "PDF Timetable API Running!"

@app.route("/pdf", methods=["POST"])
def pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    return jsonify({
        "success": True,
        "filename": file.filename,
        "message": "PDF received successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
