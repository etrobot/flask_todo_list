import logging

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask_login import current_user, login_required

from App.controllers import (
    jwt_required,
    getFreeAccountId,
    getRandomAccount,
    get_account,
    create_Conversation,
    get_Conversation_by_userId,
    get_Task_by_conversationId,
    get_Task,
    create_Task
)

chat_views = Blueprint('chat_views', __name__, template_folder='../templates')


@chat_views.route('/api/conversations', methods=['GET'])
@jwt_required()
def get_conversations():
    jwt_id = get_jwt_identity()
    conversations = get_Conversation_by_userId(jwt_id)
    convList=[[x['conversationId'],x['title']] for x in conversations]
    convList.reverse()
    return jsonify(convList)


@chat_views.route('/api/create_conversation', methods=['POST'])
@jwt_required()
def create_converstaion():
    jwt_id = get_jwt_identity()
    newConv = create_Conversation(jwt_id)
    return jsonify({'converstaionId': newConv.conversationId})


@chat_views.route('/api/tasks', methods=['GET'])
def get_tasks_by_conversationid():
    data = request.data
    logging.getLogger(__name__).debug(data)
    tasks = get_Task_by_conversationId(data)
    return tasks


@chat_views.route('/api/create_task', methods=['POST'])
@jwt_required()
def create_task():
    jwt_id = get_jwt_identity()
    if not jwt_id:
        return 401
    data = request.json
    accountId= getFreeAccountId()
    if accountId is not None:
        account=get_account(accountId)
    else:
        account=getRandomAccount()
    result=create_Task(conversationId=data['conversationId'],prompt=data['prompt'],account=account)
    logging.getLogger(__name__).debug('createTaskData:%s' % data)
    return jsonify({'taskId': result.id})


@chat_views.route('/api/get_task', methods=['GET'])
@jwt_required()
def get_task():
    if not get_jwt_identity():
        return 401
    data = request.args
    return get_Task_by_conversationId(data['conversationId'])
