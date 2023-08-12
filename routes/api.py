from flask import Flask, jsonify, request
from flask_cors import CORS
from app.middlewares.auth_middleware import authControl

app = Flask(__name__)
CORS(app)

from app.controllers.log_controller import getlogsForUser, createLogForUser

@app.route('/api/logs', methods=['GET'])
def apiGetlogsForUser():
    authControl(request.headers)
    return getlogsForUser(request.headers.get('userId'))

@app.route('/api/logs', methods=['POST'])
def apiCreateLogForUser():
    authControl(request.headers)
    return createLogForUser(request.headers.get('userId'), request.get_json())
