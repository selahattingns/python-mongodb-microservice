from flask import jsonify

# @param userId
def getlogsForUser(userId):
    return jsonify({
                           "id": userId,
                           "name": "Örnek 1"
                       })

# @param data
def createLogForUser(data):
    return jsonify(data)
