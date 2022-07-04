
let hello = prompt ("give words with commas")
let arr = hello.split(",")
console.log (arr)

let z = null
//findining longest length
for (var i = 0; i < arr.length; i++) {
    let x = arr[i].length  //1  2  
    //let y = arr [i + 1].length	//2  3
  	if (x > z) {
  		z = x
  	}
 	
 

}
console.log (z)

let s = "*"
let space = " "	

console.log (s.repeat(z+2))

for (var i = 0; i < arr.length; i++) {
	let x = arr[i].length
	if (x == z) {
		console.log (s + arr[i] + s)
	}
	else {
		let a = z - x
		console.log (s + arr[i] + space.repeat(a) + s)
	}
}

console.log (s.repeat(z+2))