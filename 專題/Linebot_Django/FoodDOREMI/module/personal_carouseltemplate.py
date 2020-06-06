from linebot.models import TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,TextSendMessage,\
    PostbackTemplateAction,ConfirmTemplate,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn
from linebot import LineBotApi
from django.conf import settings
import random

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN) #到Setting檔 讀出TOKEN


#post data只能限於0-300 太長ERROR
#不能用函數 ， Linebot 的設計關西 參數後面不能再用函數 抓不到 所以用list



def template_choice(name_list,event,word):
    # 判斷推薦回去給使用者的個數
    if len(name_list) >= 5:
        name_list = random.sample(name_list, k=5)
    elif len(name_list) == 0:
        if word == "search":
            message=TextSendMessage(text="抱歉，資料庫找不到包含輸入條件的食譜")
            line_bot_api.reply_message(event.reply_token, message)
        elif word == "personal":
            message = TextSendMessage(text="抱歉，資料庫找不到可推薦的食譜")
            line_bot_api.reply_message(event.reply_token, message)
    Columnlist = []
    for data in name_list:
        Columnlist.append(CarouselColumn(
            thumbnail_image_url=str(data['recipe_img_url']),
            title=str(data["recipe_name"]),
            text="請選擇",
            actions=[
                PostbackTemplateAction(
                    label="食材",
                    data="data=sendinfo&value=0&name=" + str(data["recipe_name"])
                ),
                PostbackTemplateAction(
                    label="步驟",
                    data="data=sendinfo&value=1&name="+ str(data["recipe_name"])
                ),
                PostbackTemplateAction(
                    label="營養成分",
                    data="data=sendinfo&value=2&name="+ str(data["recipe_name"])
                )
            ]))
    message = TemplateSendMessage(
        alt_text='無法顯示',
        template=CarouselTemplate(columns=Columnlist))
    try:
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤00"))


