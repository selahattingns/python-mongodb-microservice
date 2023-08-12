from flask import Flask, jsonify, request
app = Flask(__name__)

from app.controllers.log_controller import getlogsForUser, createLogForUser

@app.route('/api/logs/<userId>', methods=['GET'])
def apiGetlogsForUser(userId):
    return getlogsForUser(userId)

@app.route('/api/logs', methods=['POST'])
def apiCreateLogForUser():
    data = request.get_json()
    return createLogForUser(data)
