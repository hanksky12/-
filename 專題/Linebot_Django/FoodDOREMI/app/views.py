from django.conf import settings
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError,LineBotApiError
from linebot.models import MessageEvent,TextSendMessage,JoinEvent,PostbackEvent,TextMessage,FollowEvent
from urllib.parse import parse_qsl
from module import personal,search,other
import re


import random

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN) #到Setting檔 讀出TOKEN
parser=WebhookParser(settings.LINE_CHANNEL_SECRET) #到Setting檔 讀出SECRET


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature=request.META['HTTP_X_LINE_SIGNATURE']
        body=request.body.decode('utf-8')

        try:
            events=parser.parse(body,signature)
        #例外處理
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        #將USER的Message回應
        for event in events:
            if isinstance(event,MessageEvent):
                if isinstance(event.message, TextMessage):
                    a = event.message.text
                    if re.findall(r'@.*',a):
                        if a == '@個人推薦':
                            personal.main(event)
                        elif a == '@搜尋':
                            search.main(event)
                        elif a == '@相關資料':
                            other.main(event)
                        elif a == '@開始測驗':
                            initial_value=random.randrange(20)#隨機初始值 不等於0
                            personal.start(event,initial_value,0)
                        elif a == "@為您推薦":
                            personal.analysis(event)
                        elif a == "@清空資料":
                            personal.clean(event)
                        elif a == "@開始搜尋":
                            search.ps(event)
                        elif a == "@文字探勘":
                            other.text_mining(event)
                        elif a == "@食材查詢":
                            search.ingredients_search(event)
                        elif a == "@用具或料理方式查詢":
                            search.tool_search(event)
                        elif a == "@混合查詢":
                            search.mix(event)
                        else:#不對相關資料的文字再做處理
                            pass
                    #使用者搜尋食材、器具、料理方式專用
                    elif re.findall(r"[_#]{1}.?[^#_]*",a):
                        ingredients_list=re.findall(r'[_#]{1}.?[^#_]*', a)
                        search.search(event,ingredients_list)
                    else:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="抱歉，您輸入了DoReMi無法理解的字串"))
            elif isinstance(event,PostbackEvent):
                backdata=dict(parse_qsl(event.postback.data))
                data = backdata.get('data')
                #處理喜好問題
                if data == "like":
                    #注意 抓出來都是STR  在需要的時候要轉int
                    value=backdata.get('value')
                    number = backdata.get('number')
                    like = backdata.get('like')
                    user = line_bot_api.get_profile(event.source.user_id)
                    #用like來判斷user
                    if int(like) == 1:
                        personal.like(value,user)
                    elif int(like) == 0:
                        personal.dislike(user)
                    else:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))
                    personal.start(event,int(value),int(number))
                #處理推薦資料的回傳
                elif data == "sendinfo":
                    value = backdata.get('value')
                    name = backdata.get('name')
                    if int(value) == 0:
                        personal.ingredients(event,name)
                    elif int(value) == 1:
                        personal.cooking_steps(event,name)
                    elif int(value) == 2:
                        personal.nutrition(event,name)
                    else:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))
                elif data == "cloud":
                    other.cloud(event)
        return HttpResponse()

    else:
        return HttpResponseBadRequest()

