from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas URI (USE ENV VARIABLE IN REAL PROJECTS)
MONGO_URI = "mongodb+srv://lowaCase1:kingp77h@cluster0.x5j7q0z.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

# Database and collection from your screenshot
db = client["health_jobs"]
jobs = db["health_jobs"]


@app.route("/")
def index():
    jobs_list = list(jobs.find().limit(276))
    return render_template("index.html", jobs=jobs_list)


if __name__ == "__main__":
    app.run(debug=True)