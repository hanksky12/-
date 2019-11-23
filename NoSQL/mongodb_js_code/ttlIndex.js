
var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

var findAllAndShow = function(coll_name){
	print('call findAll');
	var cursor = db[coll_name].find({});
    showCursorItems(cursor);
}

var db = db.getSisterDB("db104");

// db.ttl_coll.drop();

// db.ttl_coll.ensureIndex({lastUpdated:1},{expireAfterSeconds:10})

// for(i = 0; i < 10 ; i++){
// 	db.ttl_coll.insert({x:i,lastUpdated:new Date()})
// }

// findAllAndShow('ttl_coll');




