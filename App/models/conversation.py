from App.database import db

class Conversation(db.Model):
    """Model for conversation table."""

    __tablename__ = 'conversation'

    conversationId = db.Column(db.Integer, primary_key=True)
    createTime = db.Column(db.DateTime)
    userId = db.Column(db.Integer)
    title = db.Column(db.String(100))
    remark = db.Column(db.String(1000))
    updateTime = db.Column(db.DateTime)
