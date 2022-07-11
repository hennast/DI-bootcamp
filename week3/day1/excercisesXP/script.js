let divs = document.getElementsByTagName("Div")
console.log(divs)

let ul = document.getElementsByTagName("ul")

 console.log(ul[0])
 console.log(ul[1])
 let li = document.getElementsByTagName("li")
 console.log(li)

 li[1].innerText = "richard"
 li[0].innerText = "henna"
 li[2].innerText = "henna"
ul[1].removeChild(li[3])
ul[2].style.backgroundColor = "lightBlue"
ul[2].removeChild(li[5])