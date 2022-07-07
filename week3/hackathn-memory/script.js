// create x amount of divs
// place them on grid as colored square

let game = document.getElementById("Memorygame")
console.log(game)

for (var i = 0; i < 16; i++) {
	 let div = document.createElement('div');
	 div.id = "tile"
	 div.classList.add ("number"+ i)
	 div.classList.add ("box")
	 game.appendChild(div)
	 div.style.backgroundColor = "blue"
	 div.style.height = 135 + 'px'

	 console.log(div)
	
}

// when clicked - show image
// check image - when 2nd image is clicked if they are the same nothing happens
// if the images are different, go back to image
// if all divs show an image display "congrats"


