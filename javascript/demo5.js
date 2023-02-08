// // math is an object in js

// console.log(Math.pow(10,2));
// console.log(Math.random());
// console.log(Math.sqrt(25));

// console.log(Math.floor(6.322233));
// console.log(Math.floor(6.822233));
// console.log(Math.ceil(6.123));
// console.log(Math.ceil(6.923));
// console.log(Math.round(6.123));
// console.log(Math.round(6.890));

// date object

// var date = new Date()

// console.log("the date is",date);
// console.log("the day is",date.getDay());
// console.log("the month is",date.getMonth());
// console.log("the date is",date.getDate());
// console.log("the year is",date.getFullYear());
// console.log("the time is",date.getTime());
// console.log("the minute is",date.getMinutes());
// console.log("the full hours  is",date.getHours());
// console.log("the seconds is",date.getSeconds());
// console.log("the time zone is",date.getTimezoneOffset());

// let const var

// var ->
// *) declred by using var keyword
// *) global scope
// *) when variabble is declared by using var keyword  it can be exicuted both inside and outside scope
// *) we can declare variable without initialization;
// var a
// a = 10
// *) we can declare the two variable with same name
// var a = 10;
// var a = 20;
// *) we can reassign the variable
// var a = 10;
// a = 20

// ex
// {
//     var a = 10;
//     console.log(a); //give result
// }
// console.log(a); // give result

// let ->
// *) declared by using let keyword
// *) block scope
// *) when varible is declared by using let keyword it can be executed only inside the scope
// *) we can declare variable without initialization;
// let c;
// c = 10
// *) we can not declare the two variable with same name
// let b = 10;
// let b = 20;
// *) we can reassign the variable
// var a = 10;
// a = 20


// ex
// {
//     var a = 10;
// }
// console.log(a); // give error

// const ->
// *) declared by using const keyword
// *) block scope
// *) same as let
// *) we can not declare variable without initialization both declartion and initialization done in same line
// const c; 
// c= 30 gives error 

// *) we can not declare the two variable with same name
// const c = 10;
// const c = 20;
// *) we can not reassign the variable
// let b = 10
// b = 20

// ex

// ex
// {
//     var a = 10;
// }
// console.log(a); // give error
