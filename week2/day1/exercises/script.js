// exercise 1
let food = "chocolate";
let meal = "breakfast";
console.log ("I eat" + " " + food + " "+ "for" + " " +  meal);

// exercise 2
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length ;
console.log (myWatchedSeriesLength);
let myWatchedSeriesSentence = "I watched 3 series";
console.log (myWatchedSeriesSentence + " " + myWatchedSeries[0] + " " + myWatchedSeries[1]+ " "+ "and"+ " "+ myWatchedSeries[2] );
myWatchedSeries.splice (2,2, "friends");
myWatchedSeries.push ("parks and rec");
myWatchedSeries.splice (0, 0, "Shera");
myWatchedSeries.splice (1, 1);
let x = myWatchedSeries[1];
console.log (x.substring(2,3));
console.log (myWatchedSeries);

//exercise 3
 let cels;
  cels = 7;
let far = cels * 9 / 5 + 32 ;

console.log (cels + "degrees celsius is" + " " + far + " " + " degrees farenheit") ; 



//exercise 4
  let c;
    let a = 34;
    let b = 21;

    console.log(a+b); //first expression
    // Prediction: 55
    // Actual: 55

     a = 2;

    console.log(a+b); //second expression
    // Prediction: 23 bc of new a
    // Actual: 23

// exercise 5
//console.log (typeof(15))
// Prediction: number
// Actual: number

//console.log(typeof(5.5))
// Prediction: number
// Actual: number

//console.log(typeof(NaN))
// Prediction: string
// Actual: number

//console.log(typeof("hello"))
// Prediction: string
// Actual: string

//console.log(typeof(true))
// Prediction: boolean
// Actual: boolean

//console.log(typeof(1 != 2))
// Prediction: number
// Actual: boolean

//console.log("hamburger" + "s")
// Prediction: hamburgers
// Actual: hamburgers

//console.log("hamburgers" - "s")
// Prediction: hamburger
// Actual: NaN

//console.log("1" + "3")
// Prediction: 1 3
// Actual:13

//console.log("1" - "3")
// Prediction:NaN
// Actual: -2

//console.log("johnny" + 5)
// Prediction: johnny5 
// Actual: johnny5

//console.log("johnny" - 5)
// Prediction: NaN
// Actual: NaN

console.log(99 * "hello");
// Prediction: NaN
// Actual: NaN

console.log(1 != 1)
// Prediction: false
// Actual: false

console.log(1 == "1")
// Prediction: true
// Actual: false

console.log(1 === "1")
// Prediction: false
// Actual: false

console.log (5 + "34")
// Prediction: 534
// Actual: 53

console.log (5 - "4")
// Prediction: 1
// Actual: 1

console.log (10 % 5)
// Prediction: 0
// Actual: 0

console.log (5 % 10)
// Prediction: 5
// Actual: 5

console.log ("Java" + "Script")
// Prediction: JavaScript
// Actual: JavaScript

console.log (" " + " ")
// Prediction:  
// Actual:

console.log(" " + 0)
// Prediction: 0
// Actual: 0

console.log(true + true)
// Prediction: true
// Actual: 2

console.log(true + false)
// Prediction: false
// Actual: 1

console.log(false + true)
// Prediction: false
// Actual: 1

console.log (false - true)
// Prediction: false
// Actual: -1 

console.log (!true)
// Prediction: false
// Actual: false

console.log (3 - 4)
// Prediction: -1
// Actual: -1

console.log ("Bob" - "bill")
// Prediction: NaN
// Actual: NaN