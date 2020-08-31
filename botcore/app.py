# import json
# 
# 
# def lambda_handler(event, context):
# 
#     return {
#         "statusCode": 200,
#         "body": json.dumps(event),
#     }
#

import json
import os
from urllib.parse import parse_qs

def lambda_handler(event, context):
    token = os.environ['SLACK_TOKEN']
    query = parse_qs(event.get('body') or '')
    if query.get('token', [''])[0] != token:
        # 予期しない呼び出し。400 Bad Requestを返す
        return { 'statusCode': 400 }
    slackbot_name = 'slackbot'
    if query.get('user_name', [slackbot_name])[0] == slackbot_name:
        # Botによる書き込み。無限ループを避けるために、何も書き込まない
        return { 'statusCode': 200 }
    # textの内容をそのまま書き込む
    return {
        'statusCode': 200,
        'body': json.dumps({
            'text': query.get('text', [''])[0]
        }) } 