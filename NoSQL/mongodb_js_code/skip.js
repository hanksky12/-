var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

var db = db.getSisterDB("db104");
db.usersRandom.drop()
var start = (new Date()).getTime();

 for(i = 0; i<1000; i++){
 	db.usersRandom.insert(
 		{
 			i:i,
 			username:'user'+i,
 			random: Math.random()
 		}
 	);
 }

 print('spend: '+ ((new Date()).getTime() - start) + ' ms');


var useGtOrLtToRandomFindUser = function(){
	var random = Math.random();
	print("random:"+random);
	var result = db.usersRandom.findOne({random:{$gt:random}})
	if(result == null){
		result = db.usersRandom.findOne({random:{$lt:random}})
	}
	printjson(result);
}

for(i = 0 ; i < 10; i++){
	useGtOrLtToRandomFindUser();
}


// var useSkipToRandomFindUser2 = function(){
// 	var total = db.usersRandom.count();
// 	var random = Math.floor(Math.random() * total);
// 	print("----->>random<<-----:"+random);
// 	var result = db.usersRandom.findOne({i:random})
// 	printjson(result)
// }

// for(i = 0 ; i < 10; i++){
// 	useSkipToRandomFindUser();
// }


