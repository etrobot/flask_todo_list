from App.database import db

class Account(db.Model):
    """Model for account table."""

    __tablename__ = 'account'

    accountId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    serverId=db.Column(db.Integer)
    channleId=db.Column(db.Integer)
    createTime = db.Column(db.DateTime)
    token = db.Column(db.String(100))
    status = db.Column(db.Integer)
    remark = db.Column(db.String(1000))
    updateTime = db.Column(db.DateTime)


