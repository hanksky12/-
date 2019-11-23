
var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

var db = db.getSisterDB("db104");

db.food.drop();

db.food.insert({_id:1,fruit:['apple','cherry','banana']});
db.food.insert({_id:2,fruit:['apple','watermelon','orange']});
db.food.insert({_id:3,fruit:['cherry','banana','apple']});
db.food.insert({_id:4,fruit:['cherry','apple']});
db.food.insert({_id:5,fruit:['apple','cherry']});
//下面這個寫法是value 跟之前的list不同會造成coding困擾建議還是用list包起來
//db.food.insert({_id:6,fruit:'banana'});


cursor = db.food.find();
showCursorItems(cursor);


// cursor = db.food.find({fruit:'banana'});
// showCursorItems(cursor);


// print("fruit.0':'cherry' ---找第0個是cherry----------------------------------------")
// cursor = db.food.find({"fruit.0":'cherry'});
// showCursorItems(cursor);


// print("{fruit:{$all:['apple','cherry']} -list裡面有就抓出來--與-{fruit:['apple','cherry']}-只會抓限定順序一模一樣----")
// cursor = db.food.find({fruit:['apple','cherry']})
// // cursor = db.food.find({fruit:{$all:['apple','cherry']}}
// // );
// // print(cursor);
// showCursorItems(cursor);

// print("{fruit:{$size:3}} -----找list裡面三個的，但無法用大於小於抓list長度---請看p31-在創json時多件一個欄位紀錄list長度，用$push和$inc保證原子性----------------------------------")
// cursor = db.food.find({fruit:{$size:3}});
// showCursorItems(cursor);

// print("{fruit:{$slice:2}}--只看list前兩個元素-----從1開始------------------------------------")
// cursor = db.food.find({},{fruit:{$slice:2}});
// showCursorItems(cursor);

// print("{$slice:-1}} ----只看list從後面算第一個元素-----從-1開始---------------------------------------")
// cursor = db.food.find({},{fruit:{$slice:-1}});
// showCursorItems(cursor);


// print("{$slice:[1,2]},_id:0} --index從0開始算----從index開始，算幾個-------------------------------------")
// cursor = db.food.find({},{fruit:{$slice:[1,2]},_id:0});
// showCursorItems(cursor);




var f = function(x){
	print(x * 2)
};


//foreach 吃一個funtion，把list裡面元素一個一個丟進去
// [3,4,5,6,7,8].forEach(f);
//類似py 的lamba 
// [3,4,5,6,7,8].forEach((x) => print(x*2));

//var fun = function(x){print(x*2);}

//[3,4,5,6,7,8].forEach(function(x){print(x*2);});




print("foreach-------------------------------------------")
cursor = db.food.find({fruit:'banana'});
// // //print(cursor);
//把資料蒐集到cursor，用fun呼叫fun印出字串，這邊注意json._id跟json.fruit寫法
cursor.forEach(function(json){ print('first furit:['+json.fruit[0]+"] (_id:"+json._id+")");})
//cursor.forEach(function(json){ printjson(json)})

// cursor.forEach((data) =>  print(`
// first 	
// 	furit:[ ${data.fruit} ] 
// 	(_id:
// 	${data._id})`))


