from flask import jsonify

def get_resource():
    return jsonify({
                           "id": 1,
                           "name": "Örnek 1"
                       })


def get_resource2():
    return jsonify({
                           "id": 2,
                           "name": "Örnek 2"
                       })
