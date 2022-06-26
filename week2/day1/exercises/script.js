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
console.log (myWatchedSeries [1]);
console.log (myWatchedSeries);

//exercise 4
  let c;
    let a = 34;
    let b = 21;

    console.log(a+b); //first expression
    // Prediction: 55
    // Actual:

     a = 2;

    console.log(a+b); //second expression
    // Prediction: 23 bc of new a
    // Actual: