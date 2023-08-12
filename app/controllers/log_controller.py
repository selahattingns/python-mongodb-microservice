from flask import jsonify
from app.middlewares.auth_middleware import authControl


# @param userId
def getlogsForUser(userId):
    authControl()

    return jsonify({
                           "id": userId,
                           "name": "Örnek 1"
                       })


# @param data
def createLogForUser(data):
    authControl()

    return jsonify(data)
