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
    originalPrompt = db.Column(db.String(500))
    improvePrompt = db.Column(db.String(500))
    getResultTime = db.Column(db.DateTime)
    resultInfo = db.Column(db.String(1000))
    resultUrl01 = db.Column(db.String(500))
    resultUrl02 = db.Column(db.String(500))
    resultUrl03 = db.Column(db.String(500))
    status = db.Column(db.Integer)
    updateTime = db.Column(db.DateTime)
    updateInfo = db.Column(db.String(1000))
    remark = db.Column(db.String(1000))

    conversation = db.relationship('Conversation', backref=db.backref('tasks', lazy=True))
    account = db.relationship('Account', backref=db.backref('tasks', lazy=True))