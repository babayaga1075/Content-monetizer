from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection
database_name = 'tutorials'
client = MongoClient('mongodb://localhost:27017/')
db = client[database_name]

@app.route('/api/tutorials', methods=['GET'])
def get_tutorials():
    # Sample route to get tutorials
    tutorials = db.tutorials.find()  # Fetch tutorials from the database
    return jsonify([tutorial for tutorial in tutorials])

@app.route('/api/ads', methods=['GET'])
def get_ads():
    # Sample route to get ads
    ads = db.ads.find()  # Fetch ads from the database
    return jsonify([ad for ad in ads])

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode