import logging

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask_login import current_user, login_required

from App.controllers import (
    jwt_required,
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
    return jsonify([[x['conversationId'],x['title']] for x in conversations])


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


@chat_views.route('/api/create_task', methods=['GET'])
@jwt_required()
def create_task():
    current_user_id = current_user.get_id()
    jwt_id = get_jwt_identity()
    if current_user_id != jwt_id:
        return jsonify({'msg': 'Invalid credentials'}), 401
    data = request.data
    logging.getLogger(__name__).debug('createTaskData:%s' % data)
    return jsonify({'taskId': create_Task(data)})


@chat_views.route('/api/get_task', methods=['GET'])
def get_task():
    data = request.data
    logging.getLogger(__name__).debug('getTaskData:%s' % data)
    return get_Task(data)
