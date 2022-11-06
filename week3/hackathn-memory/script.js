// create x amount of divs
// place them on grid as colored square
// when clicked - show image
// check image - when 2nd image is clicked if they are the same nothing happens
// if the images are different, go back to image

let game = document.getElementById("Memorygame")


//score calculator 
let score = document.getElementsByClassName('score')[0]
console.log(score)
let x = 0 
score.textContent = x

//array of pictures
let pics = ["banana.jpg", "strawberry.jpg", 
			 "strawberry.jpg", 
			"apple.png", "kiwi.jpg", "cherry.png",  
			 "watermelon.png", "pear.jpg", "apple.png", "kiwi.jpg", 
			"pear.jpg","banana.jpg", "lemon.png",
			  "cherry.png",
			"lemon.png", "watermelon.png"]
pics.sort(function(a, b){return 0.5 - Math.random()}); // shuffle the pictures each time they come on screen
let Check = []

for (var i = 0; i < 16; i++) {
	 let div = document.createElement('div');
	 div.id = "tile"
	 div.classList.add ("box")
	 game.appendChild(div)
	 div.style.backgroundColor = "blue"
	 div.style.height = 135 + 'px'        /// up until here creating the grid itself, the 'cards'
	 let img = document.createElement('img')   //adding invisble pics to the element
	 img.setAttribute('src', pics[i])
	 img.classList.add ("hide")
	 img.id = pics[i]
	 img.style.height = 100 + 'px'
	 img.style.margin = 'auto'
	 img.style.marginTop = 6 + 'px'
	 div.appendChild (img)
	
	 div.addEventListener('click',function(){
	 	if (div.style.backgroundColor == 'blue'){ //this makes sure if the match is already found it can't be used again
	 	
	 	
	 	div.firstElementChild.style.display = 'block' //once the div is clicked you can see the fruit
	 	
	 	if (Check.includes(img)) // now we check if we have already executed the following loop with this div so we know we are using 2 unique images
	 	{}
	 	else { //if it is unique, continue
	 	Check.push (img)
	 	
	 	if (Check.length == 2){ // see that there are 2 tiles
	 		
	 		if (Check[0].src == Check[1].src) { //check if it is the same image
	 			console.log("match")
	 			Check[0].parentElement.style.backgroundColor = 'white' //removing the first tile of match
	 			Check[0].style.display = 'none'
	 			Check[1].parentElement.style.backgroundColor = 'white' //removing second tile of match
	 			Check[1].style.display = 'none' 
	 			
	 			Check.splice(0, 2) //clears the array so more elements can be checked
	 			x++ //adds one to your score
	 			score.textContent = x //displays that on screen
	 			if (x == 8) { //let's user know they have won 
					alert('you win')


					}
	 			
	 			}
	 		else { //this is if their are 2 elements in the array but they are not the same

	 			console.log('not a match')
	 			setTimeout(()=>{ //gives player time to see what they got
				Check[0].style.display = 'none'
	 			Check[1].style.display = 'none'
	 			Check.splice(0, 2)
	 			},1500)
	 			

	 			
	 			}

	 	}
	 	}
	 }
	 
	 })
	
	
}

let instr = document.getElementsByClassName('instructions')[0] //to create a button that will allow user to learn the instruction

instr.addEventListener("click", function() {
		console.log(instr)  
		alert("To play\n1. click on two tiles\n2. if tiles ar a match, they will remain picture side up\n3.if pictures are not a match, they will revert to tile\n4.Remember where the picture is to get all 8 matches\n GOOD LUCK!!")
});

let newGame = document.getElementsByClassName ('newgame')[0] // button to reload game from inside
console.log(newGame)
newGame.addEventListener ('click', function(){
	let y = confirm('this will reload page') //warns user
	if (y == true) {
		window.location.reload()
	}
	
})


