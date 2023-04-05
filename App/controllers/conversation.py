from App.models import Conversation
from App.database import db
from datetime import *

def create_Conversation(userId):
    newConversation = Conversation(userId=userId,title=datetime.now().strftime('%Y-%m-%d %H:%M'))
    db.session.add(newConversation)
    db.session.commit()
    return newConversation

def get_Conversation_by_userId(userId):
    return [x.get_json() for x in Conversation.query.filter_by(userId=userId).all()]

def update_Conversation(id, Conversationname):
    conversation = Conversation.query.filter_by(conversationId=id).first()
    if conversation:
        Conversation.Conversationname = Conversationname
        db.session.add(Conversation)
        return db.session.commit()
    return None
    