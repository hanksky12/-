// db = connect("localhost:27017/db104");

var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

db.food2.drop()

db.food2.insert({apple:1,banana:2,peach:2});

db.food2.insert({apple:1,spinach:30,watermelon:3,a:1,c:78})

// print("----看不到裡面print的字串，因為把fun送到伺服器那邊跑，client端看不到，要debug就在本地端開伺服器測試一下code比較容易debug----------------------------")
// cursor = db.food2.find({$where:function(){
// 	print("=================================")
// 	for(var current in this){
// 		for(var other in this){
// 			print(">>>>>>>------>current:"+this[current]+" other:"+this[other]);
// 			if(current != other && this[current] == this[other]){
// 				return true;
// 			}
// 		}
// 	}
// 	return false;
// }});
// showCursorItems(cursor);

// print("----上面兩個混用可在bison狀態先篩選----下面簡單但效率差----------------------")
// cursor = db.food2.find( {watermelon : {$exists:true}, $where:'this.watermelon >= 3 && this.apple > 3'} )
// cursor = db.food2.find("this.apple > 4")
// showCursorItems(cursor);


// print("----欄位大於6抓上來，會算_id進來---------------------")
// cursor = db.food2.find({$where:function(){
// 	var count = 0;
// 	for(var current in this){
// 		count++;
// 		if(count >= 6){
// 			return true;
// 		}		
// 	}
// 	return false;
// }});
// showCursorItems(cursor);

print("--value總和大於40----要去debug掉_id不是數字-----------------")
cursor = db.food2.find({$where:function(){
	var sum = 0;
	for(var current in this){
		print("current:"+current)
		if(current != '_id'){
			sum = sum + this[current];
			if(sum > 40){
				return true;
			}
		}	
	}
	return false;
}});
showCursorItems(cursor);