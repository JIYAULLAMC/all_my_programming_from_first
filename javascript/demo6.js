

let content = document.getElementById("demo")

content.textContent = "<h1>Hello World from java script</h1>"

// in above statement we can only replace the text but not tag


let content1 = document.getElementById("demo1")
console.log(content1)

content1.innerHTML = "<h2> Hello World from java script 1 </h2>"
// in above statement we can only replace the text and  tag as shown 

let content2 = document.getElementById("demo2")
console.log(content2)

content2.innerHTML = "<a href=''> Hello World from java script a </a>"
// in above statement we can only replace the text and  tag as shown 


let content5 = document.getElementById("demo5")
console.log(content5)
// we can change the
content5.style.content = "url('./book.png')"
// in above statement we can only replace the text and  tag as shown 


// ###################################################3


let forMyClass = document.getElementsByClassName("myClass")
console.log(forMyClass);
forMyClass[0].innerHTML="hello world"
forMyClass[1].style.color ="red"


//#################
// selecting by id

