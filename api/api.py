from flask import Flask, request, jsonify
from core.subscription_manager import SubscriptionManager
from data.database import Database

app = Flask(__name__)
db = Database()
subscription_manager = SubscriptionManager(db)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    user_id = request.json['user_id']
    repo_name = request.json['repo_name']
    subscription_manager.add_subscription(user_id, repo_name)
    return jsonify({"message": "Subscription added successfully"}), 200

@app.route('/subscriptions/<user_id>', methods=['GET'])
def get_subscriptions(user_id):
    subscriptions = subscription_manager.get_subscriptions(user_id)
    return jsonify({"subscriptions": subscriptions}), 200

if __name__ == '__main__':
    app.run(debug=True)
