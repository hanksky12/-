db = connect("localhost:27017/db104");

var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

db.iiiCollection.drop();

for(var i = 0; i < 100; i++){
	db.iiiCollection.insert({age:i,name:'user'+i});
}

//在mongodb裡面會自動show,在外面的commed line則不會，要自己寫
//cursor = db.iiiCollection.find({},{age:1,_id:0});
//showCursorItems(cursor);


// print('------------between the ages of 20 and 30   -----------------');
// //條件表達:用json寫法
// cursor = db.iiiCollection.find({age:{
// 									 $gte:20,
// 									 $lte:30
// 								    }
// 							    }
// 								,
// 							    {_id:0,age:1,name:1}
// 	                          );
// showCursorItems(cursor);

//條件表達:用code的寫法java script，好讀，效能不好須轉譯
// cursor = db.iiiCollection.find("this.age > 20 && this.age < 30")
// showCursorItems(cursor);


// print('------------about $in 一個一個列出來-----------------');
// cursor = db.iiiCollection.find(
// 	{age:{$in:[25,36,47,99]}},
// 	{age:1,name:1,_id:0}
// );
// showCursorItems(cursor);


// print('------------about $nin 不要的列出來-----------------');
// cursor = db.iiiCollection.find(
// 	{age:{$nin:[20,21,22,23,24,25,26,27,28,29,30]}},
// 	{age:1,name:1,_id:0}
// );
// showCursorItems(cursor);


cursor = db.iiiCollection.find(
	{"name":/^user[^1-3][1-3]$/},
	{age:1,name:1,_id:0}
);
showCursorItems(cursor);






















