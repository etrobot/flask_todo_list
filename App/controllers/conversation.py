from App.models import Conversation
from App.database import db

def create_Conversation(userId):
    newConversation = Conversation(userId=userId)
    db.session.add(newConversation)
    db.session.commit()
    return newConversation

def get_Conversation_by_userId(userId):
    return Conversation.query.filter_by(userId=userId).all()

def get_Conversation(id):
    return Conversation.query.get(id)

def get_all_Conversations():
    return Conversation.query.all()

def get_all_Conversations_json():
    Conversations = Conversation.query.all()
    if not Conversations:
        return []
    Conversations = [Conversation.get_json() for Conversation in Conversations]
    return Conversations

def update_Conversation(id, Conversationname):
    Conversation = get_Conversation(id)
    if Conversation:
        Conversation.Conversationname = Conversationname
        db.session.add(Conversation)
        return db.session.commit()
    return None
    