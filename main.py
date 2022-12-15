from flask import Flask,jsonify,request
from data import data
import csv
with open('articles.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":all_articles[0],
        "message":"success"
    }),200
@app.route("/get-articles")
def get_movie():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })
@app.route("/liked-articles", methods=["POST"])
def liked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if(__name__=="__main__"):
    app.run(debug = True)
