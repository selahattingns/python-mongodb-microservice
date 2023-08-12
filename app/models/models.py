from mongoengine import Document, StringField, IntField, DateTimeField

class LogEntry(Document):
    user_id = IntField(required=True)
    message = StringField(required=True)
    created_at = DateTimeField(required=True)