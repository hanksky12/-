from django.conf import settings
from linebot import LineBotApi
from linebot.models import TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,TextSendMessage,\
    PostbackTemplateAction,ConfirmTemplate,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn
import pymongo,json,os,re
from module import personal_carouseltemplate
path1=os.path.abspath('.\info')
with open(path1+"\info.txt",'r',encoding='utf-8') as f:
    info=json.load(f)
    host=info["mongohost"]

#mongo設定
mongo_db="food"
mongo_db_collection="fooddata"
client = pymongo.MongoClient('mongodb://%s:%s@%s:%s/' % ('sky', 'sky', host, '27017'))
mongo_db = client[mongo_db]

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN) #到Setting檔 讀出TOKEN

def main(event):
    try:
        message=TemplateSendMessage(
            alt_text='無法顯示',
            template=ButtonsTemplate(
                title='查詢介紹:',
                text="請選擇",
                actions=[MessageTemplateAction(label="食材查詢",text="@食材查詢"),
                         MessageTemplateAction(label="用具或料理方式查詢", text="@用具或料理方式查詢"),
                         MessageTemplateAction(label="混合查詢", text="@混合查詢"),
                         ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))


def tool_search(event):
    try:
        message=TemplateSendMessage(
            alt_text='無法顯示',
            template=ButtonsTemplate(
                title='使用介紹:',
                text="請將您的工具或料理方式以下面方法表示\n單一查詢 例如:#烤箱\n多個查詢 例如:#油鍋#電鍋",
                actions=[MessageTemplateAction(label="開始搜尋",text="@開始搜尋")]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))


def ingredients_search(event):
    try:
        message=TemplateSendMessage(
            alt_text='無法顯示',
            template=ButtonsTemplate(
                title='使用介紹:',
                text="請將您的食材以下面方法表示\n單一查詢 例如:_雞蛋\n多個查詢 例如:_糖_魚",
                actions=[MessageTemplateAction(label="開始搜尋",text="@開始搜尋")]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))
def mix(event):
    try:
        message=TemplateSendMessage(
            alt_text='無法顯示',
            template=ButtonsTemplate(
                title='使用介紹:',
                text="查詢食材請用:_雞蛋\n查詢工具或料理方式請用:#油鍋\n同時混合表示:_雞蛋#電鍋 或 #電鍋_雞蛋",
                actions=[MessageTemplateAction(label="開始搜尋",text="@開始搜尋")]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))

def ps(event):
    text="PS:不限制輸入的條件數量，將為您搜尋同時符合所有輸入條件的料理，請記得輸入繁體中文不要有錯別字喔!準備好後請開啟您的小鍵盤輸入"
    try:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))


def except_word(tmp,event):
    if len(tmp) == 0:#檢查符號後面  未輸入文字
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="#或_號後面面並未夾帶文字，請重新輸入"))
    elif re.findall(r"[^\u4e00-\u9fa5]", tmp):  # 檢查符號後面輸入 非繁體中文
        print(re.findall(r"[^\u4e00-\u9fa5]", tmp))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="#或_號後面夾帶了非繁體中文，請重新輸入"))
    return tmp

def search(event,tmp_list):
    #先判斷輸入的屬於哪類條件
    tool_cookstyle_list=[]
    ingredients_list=[]
    for tmp in tmp_list:
        if re.match(r"#.*", tmp):
            tmp = tmp.strip("#")
            tmp=except_word(tmp, event)
            tool_cookstyle_list.append(tmp)
        elif re.match(r"_.*", tmp):
            tmp = tmp.strip("_")
            tmp = except_word(tmp, event)
            ingredients_list.append(tmp)
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))

    #依條件做好模糊搜尋用的字典    下面3行是濃縮過的精華原本用if else判斷輸入個數 再用if判斷各種組合情況
    #1.2行生成list給mongo使用  一個list放入1~多個搜尋用的dict 最後兩邊的list加起來形成混合list 做搜尋
    search_ingredient_names = [{"ingredients.ingredient_names": {'$regex': ingredients_list[x]}} for x in range(0, len(ingredients_list))]
    search_methods = [{"cooking_steps.methods": {'$regex': tool_cookstyle_list[x]}} for x in range(0, len(tool_cookstyle_list))]
    name_list = mongo_db[mongo_db_collection].find({"$and": search_methods + search_ingredient_names})

    aname_list=list(name_list)#mongo find出來的要具現化
    print(aname_list)
    personal_carouseltemplate.template_choice(aname_list,event,"search")




