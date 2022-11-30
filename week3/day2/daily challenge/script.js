

let noun = "noun"
let userNoun =  document.getElementById('noun')
userNoun.onchange = function() {
  noun = userNoun.value; //creates variable for noun itself
  console.log(noun)
};

let adj = "adjective"
let userAdj =  document.getElementById('adjective')
userAdj.onchange = function() {
  Adj = userAdj.value; //creates variable for adj itself
  console.log(Adj)
};

let person = "person"
let userPerson =  document.getElementById('person')
userPerson.onchange = function() {
  person = userPerson.value; //creates variable for name itself
  console.log(person)
};

let verb = "verb"
let userVerb =  document.getElementById('verb')
userVerb.onchange = function() {
  verb = userVerb.value; //creates variable for verb itself
  console.log(verb)
};

let place 
let userPlace =  document.getElementById('place')
userPlace.onchange = function() {
  place = userPlace.value; //creates variable for place itself
  console.log(place)
};


//storyOne = ("Once upon a time their was a person named " + person +" they lived in " + place + " with their " + noun + " and loved to " + verb + " becuase they were very " + adj )


storySpot = document.getElementById('story') //this is the span that the story goes in
let div = document.createElement('div');
div.id = "madLib"
div.classList.add ("madLib")
storySpot.appendChild(div)

let form = document.getElementById('libform')

form.addEventListener("submit", test)

            function test(e){
              alert('submit ! ')
              e.preventDefault()
            }