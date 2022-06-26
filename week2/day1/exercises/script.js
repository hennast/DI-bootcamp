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
console.log (typeof(15))
// Prediction: number
// Actual:

console.log(typeof(5.5))
// Prediction: number
// Actual:

typeof(NaN)
// Prediction:
// Actual:

typeof("hello")
// Prediction: string
// Actual:

typeof(true)
// Prediction: boolean
// Actual:

typeof(1 != 2)
// Prediction: number
// Actual:

"hamburger" + "s"
// Prediction:
// Actual:

"hamburgers" - "s"
// Prediction:
// Actual:

"1" + "3"
// Prediction:
// Actual:

"1" - "3"
// Prediction:
// Actual:

"johnny" + 5
// Prediction:
// Actual:

"johnny" - 5
// Prediction:
// Actual:

99 * "hello"
// Prediction:
// Actual:

1 != 1
// Prediction:
// Actual:

1 == "1"
// Prediction:
// Actual:

1 === "1"
// Prediction:
// Actual: