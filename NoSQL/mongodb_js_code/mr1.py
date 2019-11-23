from bson.code import Code
import pymongo
db = pymongo.MongoClient().db103

mapper = Code("""function(){
	for(var key in this){
		if(key !== '_id'){
			emit(key,{'count':1});
		}
	}
}
""")

reducer = Code(""" 
	function(key,emits){
	total = 0;
	for(var i in emits){
		total+=emits[i].count;
	}
	return {'count':total};
}
""")

result = db.mr1.map_reduce(mapper, reducer, "mr1_result_out_collection")

for row in result.find():
    print(row)

