from 𝚃𝚢𝚙𝚘 import *
from 𝙸𝚖𝚙𝚘𝚛𝚝𝚎𝚛 import *
from 𝙱𝚊𝚜𝚜𝚎𝚌𝚘𝚗 import *

class Approvals(BASE):
    __tablename__ = "approval"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(Integer, primary_key=True)

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)  # ensure string
        self.user_id = user_id

    def __repr__(self):
        return "<Approve %s>" % self.user_id


Approvals.__table__.create(checkfirst=True)



def approve(chat_id, user_id):
    with APPROVE_INSERTION_LOCK:
        approve_user = Approvals(str(chat_id), user_id)
        SESSION.add(approve_user)
        SESSION.commit()


def is_approved(chat_id, user_id):
    try:
        return SESSION.query(Approvals).get((str(chat_id), user_id))
    finally:
        SESSION.close()


def disapprove(chat_id, user_id):
    with APPROVE_INSERTION_LOCK:
        disapprove_user = SESSION.query(Approvals).get((str(chat_id), user_id))
        if disapprove_user:
            SESSION.delete(disapprove_user)
            SESSION.commit()
            return True
        else:
            SESSION.close()
            return False


def list_approved(chat_id):
    try:
        return (
            SESSION.query(Approvals)
            .filter(Approvals.chat_id == str(chat_id))
            .order_by(Approvals.user_id.asc())
            .all()
        )
    finally:
        SESSION.close()
