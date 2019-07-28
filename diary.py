from peewee import *
import datetime
# !/user/bin/env


db = SqliteDatabase('diary.db')


class Entry(Model):
    """
    content and timestamp
    """

    class Meta:
        database = db


def add_entry():
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    pass


def view_entries():
    pass


def delete_entry():
    pass


if __name__ == "__main__":
    initialize()
    menu_loop()
