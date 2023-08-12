from flask import jsonify
from mongoengine import connect, Document, StringField, IntField, DateTimeField
from app.models.log_entry import LogEntry
import datetime


connect('python_example', host='localhost', port=27017)


# @param userId
def getlogsForUser(userId):
    all_logs = LogEntry.objects(user_id=userId)
    logs_list = []

    for log in all_logs:
        logs_list.append({
            'user_id': log.user_id,
            'message': log.message,
            'created_at': log.created_at
        })

    return jsonify(logs_list)


# @param userId
# @param data
def createLogForUser(userId, data):
    new_log = LogEntry(user_id="1", message='\'' + data['title'] + '\' message has been added', created_at=datetime.datetime.now())
    new_log.save()

    return jsonify("ok")
