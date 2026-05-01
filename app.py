@app.route("/pdf", methods=["POST"])
def pdf():
    try:
        if "file" not in request.files:
            return jsonify({"success": False, "error": "No file uploaded"}), 400

        file = request.files["file"]

        import pdfplumber
        text = ""

        with pdfplumber.open(file.stream) as pdf:
            # ★ここが超重要（最初の3ページだけ）
            for i, page in enumerate(pdf.pages):
                if i >= 3:
                    break
                text += page.extract_text() + "\n"

        return jsonify({
            "success": True,
            "text": text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
