
from flask import Flask, render_template, request, jsonify

from predicition_engine import predict_url


app = Flask(__name__)


def add_risk_display(result):
    """Add UI-related risk class and icon to prediction result."""

    if result["risk_level"] == "LOW":
        result["risk_class"] = "low"
        result["risk_icon"] = "🟢"

    elif result["risk_level"] == "MEDIUM":
        result["risk_class"] = "medium"
        result["risk_icon"] = "🟡"

    elif result["risk_level"] == "HIGH":
        result["risk_class"] = "high"
        result["risk_icon"] = "🟠"

    else:
        result["risk_class"] = "critical"
        result["risk_icon"] = "🔴"

    return result


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if url:
            result = predict_url(url)
            result = add_risk_display(result)

    return render_template(
        "index.html",
        result=result
    )


@app.route("/api/check", methods=["POST"])
def api_check():

    data = request.get_json(silent=True)

    if not data or "url" not in data:
        return jsonify({
            "error": "URL is required"
        }), 400

    url = str(data["url"]).strip()

    if not url:
        return jsonify({
            "error": "URL cannot be empty"
        }), 400

    try:

        result = predict_url(url)
        result = add_risk_display(result)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": "Unable to analyze URL",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)

