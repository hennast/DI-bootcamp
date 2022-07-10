// create x amount of divs
// place them on grid as colored square

let game = document.getElementById("Memorygame")


//score calculator 
let score = document.getElementsByClassName('score')[0]
console.log(score)
let x = 0 
score.textContent = x

let pics = ["banana.jpg", "strawberry.jpg", 
			 "strawberry.jpg", 
			"apple.png", "kiwi.jpg", "cherry.png",  
			 "watermelon.png", "pear.jpg", "apple.png", "kiwi.jpg", 
			"pear.jpg","banana.jpg", "lemon.png",
			  "cherry.png",
			"lemon.png", "watermelon.png"]
pics.sort(function(a, b){return 0.5 - Math.random()});
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
	 	if (div.style.backgroundColor == 'blue'){ 
	 	
	 	
	 	div.firstElementChild.style.display = 'block'
	 	
	 	if (Check.includes(img))
	 	{}
	 	else {
	 	Check.push (img)
	 	
	 	if (Check.length == 2){
	 		console.log (Check)
	 		if (Check[0].src == Check[1].src) {
	 			console.log("match")
	 			Check[0].parentElement.style.backgroundColor = 'white'
	 			Check[0].style.display = 'none'
	 			Check[1].parentElement.style.backgroundColor = 'white'
	 			Check[1].style.display = 'none' 
	 			event.stopPropagation() 
	 			Check.splice(0, 2)
	 			x++
	 			score.textContent = x
	 			if (x == 8) {
					alert('you win')


					}
	 			
	 			}
	 		else {

	 			console.log('not a match')
	 			setTimeout(()=>{
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

let instr = document.getElementsByClassName('instructions')[0]

instr.addEventListener("click", function() {
		console.log(instr)  
		alert("To play\n1. click on two tiles\n2. if tiles ar a match, they will remain picture side up\n3.if pictures are not a match, they will revert to tile\n4.Remember where the picture is to get all 8 matches\n GOOD LUCK!!")
});

let newGame = document.getElementsByClassName ('newgame')[0]
console.log(newGame)
newGame.addEventListener ('click', function(){
	let y = confirm('this will reload page')
	if (y == true) {
		window.location.reload()
	}
	
})

// when clicked - show image


// check image - when 2nd image is clicked if they are the same nothing happens
// if the images are different, go back to image
