from flask import Flask, render_template, request

from predicition_engine import predict_url


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if url:
            result = predict_url(url)

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

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)