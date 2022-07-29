function infoAboutMe() {
	console.log("my name is henna")
}

infoAboutMe ()
console.log ("PART 2")

//Create a function named calculateTip() that takes no parameter.
//Inside the function, ask John for the amount of the bill.
//Here are the rules

//If the bill is less than $50, tip 20%.
//If the bill is between $50 and $200, tip 15%.
//If the bill is more than $200, tip 10%.
//Console.log the tip amount and the final bill (bill + tip).
//Call the calculateTip() function.

function calculateTip() {
	let bill = prompt ("please enter total bill")
	bill = parseInt(bill)
	if (bill < 50) {
		
		bill = bill + (bill * .2)
	}
	if (bill >= 50 && bill <= 200) {
		bill = bill + (bill * .15)
	}
	else {
		bill = bill + (bill * .1)
	}
	console.log (bill.toFixed(2))
}

calculateTip()

console.log ("PART 3")

//Create a function call isDivisible() that takes no parameter.
//In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
//At the end, console.log the sum of all numbers that are divisible by 23.
function isDiviible (){
	let x = null
	for (var i = 0; i < 500; i++) {
		
		if (i % 23 == 0) {
		x = i + x
		console.log(i)
		}
		
	}
	console.log (x)
}

isDiviible ()

//let x = 0
//while (x < 500) {
//	x++
//	let sum;
//	if (x % 23 == 0) {
//		
//		console.log(x)

//	}
	

//}

console.log ("PART 5")
//Add the stock and prices objects to your js file.

//Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

//Create a function called myBill() that takes no parameters.

//The function should return the total price of your shoppingList. In order to do this you must follow these rules:
//The item must be in stock. (Hint : check out if .. in)
//If the item is in stock find out the price in the prices object.

//Call the myBill() function.

//Bonus: If the item is in stock, decrease the item’s stock by 1



//let stock = { 
 //   "banana": 6, 
   // "apple": 0,
 //   "pear": 12,
 //   "orange": 32,
//    "blueberry":1
//}  

//let prices = {    
//    "banana": 4, 
//    "apple": 2, 
//    "pear": 1,
//    "orange": 1.5,
//    "blueberry":10
//} 
//let shoppingList = ["banana", "orange", "apple"]

//function myBill () {
	//we need a variable x to have index(x) so x=0 while x < .length 
	

 //for (var i = 0; i < shoppingList.length; i++) {
  
 // if(stock[shoppingList[i] > 0 ){
  //  console.log (7)
 // }
//}

//myBill()
console.log ("PART 6")