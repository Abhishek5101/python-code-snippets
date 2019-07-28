from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    """
    contnet and timestamp
    """

    class Meta:
        database = db


def add_entry():
    pass


def view_entries():
    pass


def delete_entry():
    pass


if __name__ == "__main__":
    menu_loop()