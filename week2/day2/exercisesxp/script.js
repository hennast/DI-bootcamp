//Create 2 variables, x and y. Each of them should have a different numeric value.
//Write an if/else statement that checks which number is bigger.

let x = 5;
let y = 2;
if ( x > y) {
	document.write ("x is the bigger number")
}


//Create a variable called newDog where it’s value is “Chihuahua”.
//Check and display how many letters are in newDog.
//Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
//Check if the variable newDog is equal to “Chihuahua”
	//if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
	//else, console.log ‘I dont care, I prefer cats’
 let newDog = "chihuahua"
document.write (newDog.length)
console.log (newDog. toLowerCase())
console.log (newDog.toUpperCase())
if (newDog = "chihuahua") {
	console.log ("I love Chihuahuas, it’s my favorite dog breed");

}
else {
	console.log ("I dont care, I prefer cats")
}

//Prompt the user for a number and save it to a variable.
//Check whether the variable is even or odd
//If it is even, display: “x is an even number”. Where x is the actual number the user chose.
//If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
let number = prompt ("Submit a number")
console.log(number)
if (number % 2 == 0) {
	console.log ("x is an even number")
}
else {
	console.log ("x is an odd number")
}

// Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
//If there is no users (the users array is empty), console.log “no one is online”.
//If there is 1 user, console.log “<name_user> is online”.
//If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
//If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let amount = users.length
let others = users.length - 2 ;
if (amount == 0) {
	console.log ( "no one is online")
}
if (amount == 1) {
	console.log (users[0]+ " " + "is online")
}

if (amount == 2)
{
	console.log (users[0]+" "+ users[1]+ " " + "are online")
}
if (amount > 2) {
	console.log(users[0]+" "+ users[1]+ " " + "and"+ " "+ others  + " " + "others are online")
}

