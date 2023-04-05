from App.models import Account
from App.database import db
from random import randint

def get_account_by_email(email):
    return Account.query.filter_by(email=email).first()

def get_account(id):
    return Account.query.get(id)

def get_all_accounts():
    return Account.query.all()

def get_all_accounts_json():
    accounts = Account.query.all()
    if not accounts:
        return []
    accounts = [account.get_json() for account in accounts]
    return accounts

def update_account(id, token):
    account = get_account(id)
    if account:
        account.token = token
        db.session.add(account)
        return db.session.commit()
    return None

def getRandomAccount():
    return Account.query.order_by(Account.accountId).offset(randint(0, Account.query.count() - 1)).first()