# -*- coding: utf-8 -*-

import time
import pymongo
import sys
import json
# --------------------------------------------------------------------------------------------------

def load_file():
    collections = ['beef', 'chicken', 'duck', 'lamp', 'noodle', 'pork', 'rice', 'soup', 'taiwan_snacks', 
                   'vegetarian', 'japanese_cuisine', 'korean_cuisine', 'thai_cuisine', 'italian_cuisine', 
                   'hongkong_cuisine', 'french_cuisine', 'curry', 'baked', 'low_calories', 'stir_fried']

    try:
        read_categories = mongo_db[collections[0]].find()
        for i, temp in enumerate(read_categories):
            for j, temp2 in enumerate(temp['cooking_steps']):
                print(temp2['steps'])
                print(temp2['methods'])
    except:
        print(sys.exc_info())

def main():
    load_file()
    
    
if __name__ == "__main__":
    # mongo connect set
    client = pymongo.MongoClient(
        'mongodb://%s:%s@%s:%s/' % ('root', 'root', '36.228.69.179', '27017'))
    mongo_db = client.recipes_info
    
    main()