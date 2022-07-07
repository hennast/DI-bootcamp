// create x amount of divs
// place them on grid as colored square

let game = document.getElementById("Memorygame")
let match = document.getElementsByClassName ("match")


let pics = ["banana.jpg", "strawberry.jpg", 
			 "strawberry.jpg", 
			"apple.png", "kiwi.jpg", "cherry.png",  
			 "watermelon.png", "pear.jpg", "apple.png", "kiwi.jpg", 
			"pear.jpg","banana.jpg", "lemon.png",
			  "cherry.png",
			"lemon.png", "watermelon.png"]
let Check = []

for (var i = 0; i < 16; i++) {
	 let div = document.createElement('div');
	 div.id = "tile"
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
	 img.style.marginTop = 6 + 'px'
	 div.appendChild (img)
	 div.addEventListener('click',function(){
	 	div.firstElementChild.style.display = 'block'
	 	
	 	Check.push (img)
	 	
	 	if (Check.length == 2){
	 		console.log (Check)
	 		if (Check[0].src == Check[1].src) {
	 			console.log("match")
	 			Check.splice(0, 2)
	 			

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
	 	
	 })
	
}



//create array of pictures

// when clicked - show image


// check image - when 2nd image is clicked if they are the same nothing happens
// if the images are different, go back to image
