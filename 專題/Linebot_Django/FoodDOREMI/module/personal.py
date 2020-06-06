from app import models
from module import person_recommend,personal_carouseltemplate
from django.conf import settings
from linebot import LineBotApi
from linebot.models import TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,TextSendMessage,\
    PostbackTemplateAction,ConfirmTemplate,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn
import random,pymongo,json,os

path1=os.path.abspath('.\info')
with open(path1+"\info.txt",'r',encoding='utf-8') as f:
    info=json.load(f)
    Webhook=info["Webhook"]
    host=info["mongohost"]
    staticurl=info["staticurl"]



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
                title='使用介紹:',
                text='請您對以下料理依喜好做選擇，可能是食材、烹煮方式或營養成分，經過分析後，將推薦您可能喜好的料理',
                actions=[MessageTemplateAction(label="開始測驗",text="@開始測驗")]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))

#value用來記錄到TOPIC表用的id     number用來記錄這是第幾道題目 共10題(做統計)
def start(event,value,number):
    try:
        if number < 10:
            value+=1
            number+=1
            if value >20:#題庫20  繞回第一題
                value=1
            food = models.Topic.objects.get(id="t" + str(value))
            message=TemplateSendMessage(
                alt_text='無法顯示',
                template=ButtonsTemplate(
                    thumbnail_image_url=staticurl+"/topic/t"+str(value)+".jpg",
                    title=food.name,
                    text='請問您對此道料理的喜好?',
                    actions=[PostbackTemplateAction(label="喜歡",text="@喜歡",data="data=like&value="+str(value)+"&number="+str(number)+"&like=1"),
                             PostbackTemplateAction(label="不喜歡",text="@不喜歡",data="data=like&value="+str(value)+"&number="+str(number)+"&like=0")]#用0來判斷user 喜好之後的要做事情
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        elif number == 10:
            message=TemplateSendMessage(
                alt_text='無法顯示',
                template=ConfirmTemplate(
                    text='恭喜完成調查!',
                    actions=[MessageTemplateAction(label="開始分析",text="@為您推薦"),
                             MessageTemplateAction(label="剛剛有選錯...",text="@清空資料")]#用0來判斷user 喜好之後的要做事情
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤~"))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤~~"))

def like(value,user): #user存在 則把分數加進表裡面 不存在則新創
    food_topic = models.Topic.objects.get(id="t" + value)
    try:
        food_calculation = models.UsersTags.objects.get(user=user)
        models.UsersTags.objects.filter(user=user).update(
            stew=food_calculation.stew + food_topic.stew,
            steamed=food_calculation.steamed + food_topic.steamed,
            hot_pot=food_calculation.hot_pot + food_topic.hot_pot,
            stir_fry=food_calculation.stir_fry + food_topic.stir_fry,
            frying=food_calculation.frying + food_topic.frying,
            dessert=food_calculation.dessert + food_topic.dessert,
            baked=food_calculation.baked + food_topic.baked,
            flour=food_calculation.flour + food_topic.flour,
            vitamin_b12=food_calculation.vitamin_b12 + food_topic.vitamin_b12,
            vitamin_a=food_calculation.vitamin_a + food_topic.vitamin_a,
            alpha_carotene=food_calculation.alpha_carotene + food_topic.alpha_carotene,
            beta_carotene=food_calculation.beta_carotene + food_topic.beta_carotene,
            dietary_fiber=food_calculation.dietary_fiber + food_topic.dietary_fiber,
            folate=food_calculation.folate + food_topic.folate,
            vitamin_e=food_calculation.vitamin_e + food_topic.vitamin_e,
            magnesium=food_calculation.magnesium + food_topic.magnesium,
            phosphorus=food_calculation.phosphorus + food_topic.phosphorus,
            niacin=food_calculation.niacin + food_topic.niacin,
            sugar=food_calculation.sugar + food_topic.sugar,
            balance=food_calculation.balance + food_topic.balance,
            sodium=food_calculation.sodium + food_topic.sodium,
            calcium=food_calculation.calcium + food_topic.calcium,
            iron=food_calculation.iron + food_topic.iron,
            fat=food_calculation.fat + food_topic.fat,
            vitamin_c=food_calculation.vitamin_c + food_topic.vitamin_c,
            potassium=food_calculation.potassium + food_topic.potassium,
            zinc=food_calculation.zinc + food_topic.zinc)
    except:
        models.UsersTags.objects.create(user=user,
                                        stew=food_topic.stew,
                                        steamed=food_topic.steamed,
                                        hot_pot=food_topic.hot_pot,
                                        stir_fry=food_topic.stir_fry,
                                        frying=food_topic.frying,
                                        dessert=food_topic.dessert,
                                        baked=food_topic.baked,
                                        flour=food_topic.flour,
                                        vitamin_b12=food_topic.vitamin_b12,
                                        vitamin_a=food_topic.vitamin_a,
                                        alpha_carotene=food_topic.alpha_carotene,
                                        beta_carotene=food_topic.beta_carotene,
                                        dietary_fiber=food_topic.dietary_fiber,
                                        folate=food_topic.folate,
                                        vitamin_e=food_topic.vitamin_e,
                                        magnesium=food_topic.magnesium,
                                        phosphorus=food_topic.phosphorus,
                                        niacin=food_topic.niacin,
                                        sugar=food_topic.sugar,
                                        balance=food_topic.balance,
                                        sodium=food_topic.sodium,
                                        calcium=food_topic.calcium,
                                        iron=food_topic.iron,
                                        fat=food_topic.fat,
                                        vitamin_c=food_topic.vitamin_c,
                                        potassium=food_topic.potassium,
                                        zinc=food_topic.zinc)
def dislike(user):
    try:#有資料不做事
        food_calculation = models.UsersTags.objects.get(user=user)
    except:#沒資料要創角 避免連續10題不喜歡且沒紀錄
        models.UsersTags.objects.create(user=user,
                                        stew=0,
                                        steamed=0,
                                        hot_pot=0,
                                        stir_fry=0,
                                        frying=0,
                                        dessert=0,
                                        baked=0,
                                        flour=0,
                                        vitamin_b12=0,
                                        vitamin_a=0,
                                        alpha_carotene=0,
                                        beta_carotene=0,
                                        dietary_fiber=0,
                                        folate=0,
                                        vitamin_e=0,
                                        magnesium=0,
                                        phosphorus=0,
                                        niacin=0,
                                        sugar=0,
                                        balance=0,
                                        sodium=0,
                                        calcium=0,
                                        iron=0,
                                        fat=0,
                                        vitamin_c=0,
                                        potassium=0,
                                        zinc=0)
def clean(event):
    user = line_bot_api.get_profile(event.source.user_id)
    models.UsersTags.objects.filter(user=user).delete()
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="資料已清空"))

def analysis(event):
    user = line_bot_api.get_profile(event.source.user_id)
    #第一個values是django orm的方法可把多筆DATA以LIST撈上來  每筆資料都是DICT形式  第二個value取出字典所有的值
    try:
        data_tag=list(models.UsersTags.objects.filter(user=user).values()[0].values())
        text_cluster,nutrition_cluster=person_recommend.tag_compute(data_tag)
        cluster_intersection=models.Analysis.objects.filter(cluster=nutrition_cluster).values()&models.Analysis.objects.filter(text_cluster=text_cluster).values()
        top_list=random.sample(list(cluster_intersection),k=5)

        original_data_list=[]
        for food in top_list:
            name=food["recipe_name"]#SQL資料只拿名字 用去mongo抓DATA 因為ID是在SQL才做的 MONGO的RAW DATA沒有ID
            tmp = mongo_db[mongo_db_collection].find({"recipe_name": name})
            original_data_list.append(list(tmp)[0])#因為find上來的是一個疊代物件指向記憶體位置  所以這邊裡面多加list具現化
        print(len(original_data_list))
        personal_carouseltemplate.template_choice(original_data_list, event, "personal")
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))



def cooking_steps(event,name):
    tmp=mongo_db[mongo_db_collection].find({"recipe_name": name})
    ingredient_names_list=[]
    for data in list(tmp)[0]['cooking_steps']:
        ingredient_names_list.append("Step"+str(data["steps"])+".")
        ingredient_names_list.append(data["methods"])
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="["+name+"]的步驟:\n"+"\n".join(ingredient_names_list)))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))

def ingredients(event,name):
    tmp=mongo_db[mongo_db_collection].find({"recipe_name": name})
    ingredient_names_list=[]
    for data in list(tmp)[0]['ingredients']:
        ingredient_names_list.append(data["ingredient_names"])
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="["+name+"]的食材:\n"+"\n".join(ingredient_names_list)))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))

def nutrition(event,name):
    data = models.Analysis.objects.filter(recipe_name=name).values()[0]
    text="["+name+"]的營養成分:\n"+"卡路里:"+str(data["calories_kcal"])+"kcal\n蛋白質:"+str(data["protein_g"])+"g\n脂肪:"+str(data["fat_g"])+"g\n膳食纖維:"\
         +str(data["dietary_fiber_g"])+"g\n維他命A:"+str(data["vitamin_a_ug"])+"ug\n維他命C:"+str(data["vitamin_c_mg"])+\
        "mg\n胡蘿蔔素alpha:"+str(data["alpha_carotene_ug"])+"ug\n鐵:"+str(data["iron_mg"])+"mg\n鋅:"+str(data["zinc_mg"])+\
         "mg\n鈣:"+str(data["calcium_mg"])+"mg\n鈉:"+str(data["sodium_mg"])+"mg"
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤"))