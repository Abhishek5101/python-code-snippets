from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    """
    contnet and timestamp
    """

    class Meta:
        database = db
