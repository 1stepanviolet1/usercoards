from typing import Any
from pymysql import connect
from pymysql.cursors import DictCursor
from pymysql.connections import Connection
from config import (
    db_host,
    db_port,
    db_user,
    db_pwd,
    db_name
)


class ReplaceDBwithCursor:
    def __init__(self, action) -> None:
        self.action = action
    
    def __call__(self, db: Connection, *args, **kwargs):
        with db.cursor() as cursor:
            res = self.action(cursor, *args, **kwargs)
        db.commit()
        return res


def connect_to_db():
    return connect(
        host=db_host,
        port=db_port,
        user=db_user,
        passwd=db_pwd,
        database=db_name,
        cursorclass=DictCursor
    )

def close_db(db: Connection):
    db.close()


@ReplaceDBwithCursor
def delete_by_id(cursor: DictCursor, id: int):
    cursor.execute(f"DELETE FROM users WHERE {id=}")


@ReplaceDBwithCursor
def insert_data(cursor: DictCursor, username, pwd):
    cursor.execute(f"INSERT INTO users (username, pwd) VALUES ('{username}', '{pwd}')")


@ReplaceDBwithCursor
def get_id_by_username(cursor: DictCursor, username):
    cursor.execute(f"SELECT id FROM users WHERE {username=}")

    try:
        return next(cursor).get("id", -1)
    except StopIteration:
        return None


def exec_cmd(db: Connection, cmd):
    cursor = db.cursor()
    cursor.execute(cmd)
    db.commit()
    return cursor


__all__ = [
    "connect_to_db",
    "close_db",
    "delete_by_id",
    "insert_data",
    "get_id_by_username",
    "exec_cmd"
]
