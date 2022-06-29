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

//isDiviible ()