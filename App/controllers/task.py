from discord import MessageType
from App.models import Task,Account
from App.database import db
from flask import jsonify
from sqlalchemy import func
import requests

def PassPromptToSelfBot(prompt: str,serverId:int,channelId:int,token:str):
    print(prompt,serverId,channelId,token)
    payload = {"type": 2, "application_id": "936929561302675456", "guild_id": serverId,
               "channel_id": channelId, "session_id": "2fb980f65e5c9a77c96ca01f2c242cf6",
               "data": {"version": "1077969938624553050", "id": "938956540159881230", "name": "imagine", "type": 1,
                        "options": [{"type": 3, "name": "prompt", "value": prompt}],
                        "application_command": {"id": "938956540159881230",
                                                "application_id": "936929561302675456",
                                                "version": "1077969938624553050",
                                                "default_permission": True,
                                                "default_member_permissions": None,
                                                "type": 1, "nsfw": False, "name": "imagine",
                                                "description": "Create images with Midjourney",
                                                "dm_permission": True,
                                                "options": [{"type": 3, "name": "prompt",
                                                             "description": "The prompt to imagine",
                                                             "required": True}]},
                        "attachments": []}}

    header = {
        'authorization': token
    }
    response = requests.post("https://discord.com/api/v9/interactions",
                             json=payload, headers=header)
    return response

def create_Task(conversationId:int,prompt:str,account:Account):
    print('min_acc',account)
    resp=PassPromptToSelfBot(prompt,account.serverId,account.channleId,account.token)
    if resp.status_code!=204:
        return jsonify({'errAccId':account.accountId})
    msgtype={
        "default":MessageType.default,
    }
    newTask = Task(conversationId=conversationId,prompt=prompt,msgType=msgtype['default'])
    db.session.add(newTask)
    db.session.commit()
    return newTask

def getFreeAccountId():
    result = db.session.query(Task.accountId, func.count(Task.id)).filter(Task.status == 0).group_by(
        Task.accountId).all()
    print('all_account',result)
    if len(result)>0:
        min_task_count = min(result, key=lambda x: x[1])[1]
        min_account_id = [x[0] for x in result if x[1] == min_task_count][0]
        return min_account_id


def get_Task_by_conversationId(conversationId):
    # 获取特定conversationId的任务
    tasks = Task.query.filter_by(conversationId=conversationId).all()

    # 将结果转换为JSON格式
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task.id,
            'conversationId': task.conversationId,
            'createTime': task.createTime,
            'accountId': task.accountId,
            'originalPrompt': task.originalPrompt,
            'improvePrompt': task.improvePrompt,
            'getResultTime': task.getResultTime,
            'resultInfo': task.resultInfo,
            'resultUrl01': task.resultUrl01,
            'resultUrl02': task.resultUrl02,
            'resultUrl03': task.resultUrl03,
            'status': task.status,
            'updateTime': task.updateTime,
            'updateInfo': task.updateInfo,
            'remark': task.remark
        })

    # 返回JSON格式的结果
    return jsonify(task_list)

def get_Task(id):
    return Task.query.filter_by(id=id)

def get_Task_by_prompt(prompt:str):
    return Task.query.filter_by(prompt=prompt).order_by(Task.updateTime.desc()).all()

def update_Task(id, msgId,url):
    Task = get_Task(id)
    if Task:
        Task.msgId = msgId
        Task.resultUrl=url
        return db.session.commit()
    return None