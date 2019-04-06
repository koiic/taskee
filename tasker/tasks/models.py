from django.db import models
from mongoengine import Document, EmbeddedDocument, fields
import datetime as dt

class TaskInput(EmbeddedDocument):
    """ models for task """
    name = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=dt.datetime.now())
    start_date = fields.DateTimeField(required=True)
    end_date = fields.DateTimeField(required=True)


class Task(Document):
    status = fields.StringField(required=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(TaskInput))
    description = fields.StringField(required=True, null=True)
    name = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=dt.datetime.now())
    start_date = fields.DateTimeField(required=True)
    end_date = fields.DateTimeField(required=True)
