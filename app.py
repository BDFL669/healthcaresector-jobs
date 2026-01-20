from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

MONGO_URI = "mongodb+srv://lowaCase1:kingp77h@cluster0.x5j7q0z.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

db = client["health_jobs"]
jobs = db["health_jobs"]
subscribers = db["subscribers"]  # NEW collection


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        email = data.get("email")

        if not email:
            return jsonify({"success": False, "message": "Email required"}), 400

        # prevent duplicates
        if subscribers.find_one({"email": email}):
            return jsonify({"success": False, "message": "Already subscribed"}), 409

        subscribers.insert_one({
            "email": email,
            "subscribed_at": datetime.utcnow()
        })

        return jsonify({"success": True, "message": "Subscribed successfully"})

    jobs_list = list(jobs.find().limit(276))
    return render_template("index.html", jobs=jobs_list)


if __name__ == "__main__":
    app.run(debug=True)