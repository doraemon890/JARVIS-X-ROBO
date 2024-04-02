import threading

from sqlalchemy import Column, String

from JarvisRobo.modules.sql import BASE, SESSION


class JarvisChats(BASE):
    __tablename__ = "jarvis_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


JarvisChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_jarvis(chat_id):
    try:
        chat = SESSION.query(JarvisChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_jarvis(chat_id):
    with INSERTION_LOCK:
        jarvischat = SESSION.query(JarvisChats).get(str(chat_id))
        if not jarvischat:
            jarvischat = JarvisChats(str(chat_id))
        SESSION.add(jarvischat)
        SESSION.commit()


def rem_jarvis(chat_id):
    with INSERTION_LOCK:
        jarvischat = SESSION.query(JarvisChats).get(str(chat_id))
        if jarvischat:
            SESSION.delete(jarvischat)
        SESSION.commit()
