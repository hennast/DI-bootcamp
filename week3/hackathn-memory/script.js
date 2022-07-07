// create x amount of divs
// place them on grid as colored square

let game = document.getElementById("Memorygame")

let pics = ["banana.jpg", "kiwi.jpg", 
			"pear.jpg", "strawberry.jpg", 
			"apple.png", "cherry.png",
			"lemon.png", "watermelon.png", "banana.jpg", "kiwi.jpg", 
			"pear.jpg", "strawberry.jpg", 
			"apple.png", "cherry.png",
			"lemon.png", "watermelon.png"]
let Check = []

for (var i = 0; i < 16; i++) {
	 let div = document.createElement('div');
	 div.id = "tile"
	 div.classList.add ("number"+ i)
	 div.classList.add ("box")
	 game.appendChild(div)
	 div.style.backgroundColor = "blue"
	 div.style.height = 135 + 'px'
	 let img = document.createElement('img')
	 img.setAttribute('src', pics[i])
	 img.classList.add ("hide")
	 img.id = pics[i]
	 img.style.height = 100 + 'px'
	 img.style.margin = 'auto'
	 div.appendChild (img)
	 div.addEventListener('click',function(){
	 	div.firstElementChild.style.display = 'block'
	 	console.log(img)
	 	Check.push (img)
	 	
	 	if (Check.length == 2){
	 		console.log (Check)
	 		if (Check[0] = Check[1]) {
	 			console.log("match")
	 		}
	 		else {
	 			console.log('not a match')
	 		}
	 	}
	 })
	
}



//create array of pictures

// when clicked - show image


// check image - when 2nd image is clicked if they are the same nothing happens
// if the images are different, go back to image
// if all divs show an image display "congrats"