from flask import Flask, jsonify
from flask_cors import CORS
from data import teachers
from model import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route("/teachers")
def teacher_data():
    output = []
    for t in teachers:
        output.append({
            "name": t["name"],
            "score": t["score"],
            "recommended_level": get_recommendation(t["score"])
        })
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
