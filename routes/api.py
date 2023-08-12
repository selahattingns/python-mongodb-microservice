from flask import Flask, jsonify
app = Flask(__name__)

from app.controllers.example_controller import get_resource, get_resource2

@app.route('/api/resource1', methods=['GET'])
def api_get_resource(): return get_resource()

@app.route('/api/resource2', methods=['GET'])
def api_get_resource2(): return get_resource2()


