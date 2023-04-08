from App.database import db

class Task(db.Model):
    """Model for task table.
    status:{0:incomplete，1:complete,-1:error}
    """

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    conversationId = db.Column(db.Integer, db.ForeignKey('conversation.conversationId'))
    createTime = db.Column(db.DateTime)
    accountId = db.Column(db.Integer, db.ForeignKey('account.accountId'))
    prompt = db.Column(db.String(500))
    resultUrl = db.Column(db.String(1000))
    msgId = db.Column(db.Integer)
    oriMsgId = db.Column(db.Integer)
    msgType = db.Column(db.String(500))
    updateTime = db.Column(db.DateTime)
    remark = db.Column(db.String(1000))

    conversation = db.relationship('Conversation', backref=db.backref('tasks', lazy=True))
    account = db.relationship('Account', backref=db.backref('tasks', lazy=True))