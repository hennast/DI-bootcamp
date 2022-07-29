let planets = [
"Mercury", "Venus",
"Earth",
 "Mars",
 "Jupiter",
 "Saturn",
 "Uranus", 
"Neptune",
"pluto"
]
let color = ["red", "orange","yellow","green","blue","purple","gray","navy","white"]
let root = document.getElementsByClassName("listplanets")[0]
for (var i = 0; i < planets.length; i++) {
	
	let z = document.createElement("div")
	z.id = planets[i]
	z.classList.add ("planet")
	z.inerText = planets[i]
	console.log(z)
	z.style.color= 'white'
	z.style.backgroundColor=color[i]
	root.appendChild(z)

}


