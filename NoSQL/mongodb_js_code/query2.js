
var showCursorItems = function(cursor){
	while (cursor.hasNext()) {
   		printjson(cursor.next());
	}
}

var db = db.getSisterDB("db104");

db.inventory.drop();

var productA = {name: 'A', quantity: 50, price: 9,  level: 10}
var productB = {name: 'B', quantity: 20, price: 20, level: 30}
var productC = {name: 'C', quantity: 30, price: 30, level: 20}
var productD = {name: 'D', quantity: 30, price: 15, level: 50}
var productE = {name: 'E', quantity: 60, price: 13, level: 60}
var productF = {name: 'F', quantity: 80, price: 20, level:null}
var productG = {name: 'G', quantity: 50, price: 10, level:null}
var productH = {name: 'H', quantity: 10, price: 10}

db.inventory.insert([
	productA,
	productB,
	productC,
	productD,
	productE,
	productF,
	productG,
	productH
]);

cursor = db.inventory.find({},{_id:0});
showCursorItems(cursor);


// print('-----多條件用list----------or三個條件-----{$or:[{quantity:50},{price:{$gt:10,$lt:20}},{price:{$in:[9,20]}}]}-----------------')
// cursor = db.inventory.find({$or:[{quantity:50},{price:{$gt:10,$lt:20}},{price:{$in:[9,20]}}]},
// 	                        {_id:0,level:0}
// );

// showCursorItems(cursor);



// print('------------------and兩個條件---{$and:[{quantity:10},{price:10}]----------------------')
// cursor = db.inventory.find({$and:[{quantity:10},{price:10}]},
// 	                        {_id:0,level:0});
// showCursorItems(cursor);


// print('-----------------and加in----"$and":[{"quantity":{"$in":[50,30]}},{"price":10}]------------------')
// cursor = db.inventory.find( {"$and":[{"quantity":{"$in":[50,30]}},{"price":10}]},
// 	                        {_id:0});

// showCursorItems(cursor);





// print('-------------not----------{price:{$not:{$gte:20}}--------------------')
// cursor = db.inventory.find({price:{$not:{$gte:20}}},
// 	                        {_id:0,price:1,name:1}
// );
// showCursorItems(cursor);



// print('-----------------找level:null但多抓一筆-------------------------')
// cursor = db.inventory.find({level:null},{_id:0});
// showCursorItems(cursor);



print('----------------找level:null且存在----{level:{$in:[null],$exists:true}---------------------------')
cursor = db.inventory.find({level:{$in:[null],$exists:true}},
	                       {_id:0}
);
showCursorItems(cursor);
