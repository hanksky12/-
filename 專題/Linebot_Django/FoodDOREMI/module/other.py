from django.conf import settings
from linebot import LineBotApi
from linebot.models import TemplateSendMessage,ImageSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,TextSendMessage,\
    PostbackTemplateAction,ConfirmTemplate,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn
import json,os

path1=os.path.abspath('.\info')
with open(path1+"\info.txt",'r',encoding='utf-8') as f:
    info=json.load(f)
    Webhook=info["Webhook"]
    staticurl = info["staticurl"]

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN) #到Setting檔 讀出TOKEN

def main(event):
    try:
        message=TemplateSendMessage(
            alt_text='無法顯示',
            template=ButtonsTemplate(
                title='相關資料:',
                text='請選擇:',
                actions=[URITemplateAction(label="資策會小組Trello",
                                           uri="https://trello.com/b/51vJ5Zl5/db104g3"),
                        URITemplateAction(label="衛福部食藥署食品資料庫",
                                           uri="https://consumer.fda.gov.tw/Food/TFND.aspx?nodeID=178"),
                        MessageTemplateAction(label="文字探勘資料分佈",text="@文字探勘"),
                        PostbackTemplateAction(label="文字探勘文字雲", data="data=cloud")
                         ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))

def text_mining(event):
    message=TemplateSendMessage(
        alt_text='無法顯示',
        template=ButtonsTemplate(
            title='三維空間投影分布情形',
            text='請在左側欄位color by選單中，選擇fit',
            actions=[URITemplateAction(label="建議在PC開啟",
                                       uri="https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/hanksky12/0a81870638956385975359e39a310e59/raw/9ddbc2c5152e82f36a4432de86163ef4268b1d4f/config.json")
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)
def cloud(event):
    try:
        message=TemplateSendMessage(
            alt_text="無法顯示",
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url=staticurl+"/other/fisho1.jpg",
                        action=MessageTemplateAction(
                        label="第一類:",
                        text="@燉品、清蒸、火鍋類")),
                    ImageCarouselColumn(
                        image_url=staticurl+"/other/fisho2.jpg",
                        action=MessageTemplateAction(
                        label="第二類:",
                        text="@燉熱炒、油煎炸類")),
                    ImageCarouselColumn(
                        image_url=staticurl+"/other/fisho3.jpg",
                        action=MessageTemplateAction(
                        label="第三類:",
                        text="@甜點、焗烤、麵粉類")),
                ]
            )
        )



        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))