import requests
import json, time

api_key = "pat_1R6RNkXKaYJXF3oUqlf05abxpDsRSpQ7RjgqqfUA1P2d6GltBaIfW1nQyGcKGt6m"

botid = "7503045194523869236"
baseUrl = 'https://api.coze.cn/v3/chat'
headers = {
    "Authorization": f"Bearer {api_key}",
    'Content-Type': 'application/json'
}


def processQuestionAnswer(response_data):
    if response_data['code']:
        print("应答异常：", response_data['msg'])
    else:
        data = response_data['data']
        count = 0
        for item in data:
            if item['type'] == 'answer':
                print("大模型应答：", item['content'])
            elif item['type'] == 'follow_up':
                if count == 0:
                    print("您可以参考如下方式提问：")
                print(f"☆ 问题{count + 1}：", item['content'])
                count += 1


def getQuesyionAnswer(conversationID, chatID):
    params = {"bot_id": botid, "task_id": chatID}
    getChatStatusUrl = baseUrl + f'/retrieve?conversation_id={conversationID}&chat_id={chatID}&'

    while True:
        response = requests.get(getChatStatusUrl, headers=headers, params=None)
        if response.status_code == 200:
            response_data = response.json()
            print(f"response_data:\n{json.dumps(response_data, indent=4, ensure_ascii=False)}")
            status = response_data['data']['status']
            if status == 'completed':
                # 从响应中提取实际的应答内容
                getChatAnswerUrl = baseUrl + f'/message/list?chat_id={chatID}&conversation_id={conversationID}'
                response = requests.get(getChatAnswerUrl, headers=headers, params=params)
                if response.status_code == 200:
                    response_data = response.json()
                    print("模型返回数据:\n", json.dumps(response_data, indent=4, ensure_ascii=False))
                    processQuestionAnswer(response_data)
                    return True
                break
            else:
                print(f"任务仍在处理中，状态: {status}")
                time.sleep(1)  # 等待5秒后再次检查
        else:
            print(f"请求失败，状态码: {response.status_code}")
            break
    return False


def questionService(questionText):
    # 定义API的URL和授权令牌

    data = {
        "bot_id": botid,
        "user_id": "jiangwp",
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {
                "role": "user",
                "content": questionText,
                "content_type": "text"
            }
        ]
    }

    # 发送POST请求
    print(f"请求信息:{json.dumps(data, indent=4, ensure_ascii=False)}")
    response = requests.post(baseUrl, headers=headers, data=json.dumps(data))

    # 检查响应状态码
    if response.status_code == 200:
        # 解析响应内容
        response_data = response.json()
        print("响应内容:", json.dumps(response_data, indent=4, ensure_ascii=False))
        chatid = response_data['data']['id']
        answer = response_data.get("answer")
        conversation_id = response_data['data']['conversation_id']
        print(f"chatid={chatid},智能体应答: {answer}")

        getQuesyionAnswer(conversation_id, chatid)

    else:
        print("请求失败，状态码:", response.status_code)
        print("错误信息:", response.text)


questionService("学费多少")


