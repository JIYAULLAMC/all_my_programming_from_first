//operators in js -> airthematic, logical, comparision, bitwise operator

// var a = Number(prompt("Enter the value of a "))
// var b = Number(prompt("Enter the value of b "))

// var a = 10;
// var b = 20;

// Airthematic operator

// console.log(`the addition of ${a} and ${b} is ${a+b}`);
// console.log(`the substraction of ${a} and ${b} is ${a-b}`);
// console.log(`the multiplication of ${a} and ${b} is ${a*b}`);
// console.log(`the division of ${a} and ${b} is ${a/b}`);
// console.log(`the modulous of ${a} and ${b} is ${a%b}`);
// console.log(`the power of ${a} and ${b} is ${a**b}`);
// console.log(`the math.power of ${a} and ${b} is ${Math.pow(10,20)}`);

// document.write(`the addition of ${a} and ${b} is ${a+b}`,"<br/>");
// document.write(`the substraction of ${a} and ${b} is ${a-b}`,"<br/>");
// document.write(`the multiplication of ${a} and ${b} is ${a*b}`,"<br/>");
// document.write(`the division of ${a} and ${b} is ${a/b}`,"<br/>");
// document.write(`the modulous of ${a} and ${b} is ${a%b}`,"<br/>");
// document.write(`the power of ${a} and ${b} is ${a**b}`,"<br/>");
// document.write(`the math.power of ${a} and ${b} is ${Math.pow(10,20)}`,"<br/>");

// assignment operator

// var a = 10;
// var b = 20;

// console.log(`the addition of ${a} and ${b} is ${a+=b}`);
// console.log(`the substraction of ${a} and ${b} is ${a-=b}`);
// console.log(`the multiplication of ${a} and ${b} is ${a*=b}`);
// console.log(`the division of ${a} and ${b} is ${a/=b}`);
// console.log(`the modulous of ${a} and ${b} is ${a%=b}`);
// console.log(`the power of ${a} and ${b} is ${a**=b}`);
// console.log(`the math.power of ${a} and ${b} is ${Math.pow(10,20)}`);

// relational operators
// a = 10;
// b = 20;
// console.log(`the addition of ${a} and ${b} is ${a < b}`);
// console.log(`the substraction of ${a} and ${b} is ${a > b}`);
// console.log(`the multiplication of ${a} and ${b} is ${a <= b}`);
// console.log(`the division of ${a} and ${b} is ${a >= b}`);
// console.log(`the modulous of ${a} and ${b} is ${a == b}`);
// console.log(`the power of ${a} and ${b} is ${a != b}`);

// console.log((10 > 40 < 1 < 0 > 100 < 29 > 92 != 1) == 2);
// console.log((11 > 10 < 1 < 0 > 1 >= 29 > 92 != 1) === 2);

// equal to

// type coercion or type casting

// conversion of one data type into another data type is called type coercion
// two types
//  implicit type casting (js engine) and explicit type casting (developers will do)
//  the process of converting data type implicitly by js engine is know as
//  implicity type casting
// example 5="1" => 4
// in the obove example the string one is converted into number data type implicitly by js engine
//

// explicit the process of convertin one data into another using some built in methods is known as
// Number() -> help the to

// var a = Number(prompt("Enter the value of a :"))
// var b = Number(prompt("Enter the value of b :"))
// sum = a+b
// alert(`the sum of a and b is ${a+b}`)

// in the above example the prompt default value is string by using  Number() method we can
// convert string data type into number data type explicitly this proce is known as explicit type casting

// difference between ==(double equal to) and ===(strinctyle equal to)

//  ==(double equal to)
// it is a comparision operator it compares whether the value is equal or not
// here type coercion will be done i.e implicit type casting
// 5=="5" -> true here string is converting to number data type

// ===(strinctyle equal to)
// it stand for strictly equal to, it is similar to double equal to(==)
// here type coersion will not be allowed se
// 5==="5" -> false here

// 1=="true" give false
// "1" ==true gives ture
// jhghj

// concatination in js
// in js we make use o + operator to combine the string
//  it is not neccessory the two operand should be a string any one operand is string it performs concatination

// a = 10
// b = "kiya"
// console.log(a+b, b+a)

// number to number

// in the above the string mala is converted into number data type the converted number is not a valid number
// so it will return a special type of number NaN

// console.log(2+2)
// console.log(2 + "2")
// console.log("2" +2);
// console.log(3 + "3");
// console.log("2"/2);---> NaN

// console.log(23&&25);
// console.log(45 &&"23");
// console.log(""&&"");
// console.log(""&&true);
// console.log("1"&&true);
// console.log(null && "2");
// console.log(undefined && "a");
// console.log(undefined && "null");
// console.log(null && "null");
// console.log("" && 4);
// console.log(4 || 3);
// console.log("" || 4)

// In js all non zero numbers are considerd as true
// Number 0, null, NaN, ""(empty string) , undefined , all these values are considered as false when the are converted to boolean
// A no empty string is considered as true

// Note :
//  logical or ||

//  logical || behave differently is the LGS value or RHS value is non boolean
//  step 1) It convets the LHS value to BBoolean
// step 2) If the conveted LHS value is true then it returns the original value present in the LHS
// Ex console.log(10 || 20)

// step 2 : If the convetrd LHS value is false then it return the original value present in the RHS
// console.log(0||20)

// Note logical &&

// logical && behaves differently if LHS value and RHS is not Boolean
// it converts LHS value to boolean
// if the converted LHS value is false it will return LHS
// if the first operand is false then it will return the false
// "" && 3 -> ""
// if the lhs value is true then it will return rhs value
// 10 && 20 -> 20

// marks = Number(prompt("Enter the marks : "))
// // marks = 63;
// if (0 <= marks && marks <= 35) {
//   console.log("fail  ");
// } else if (35 <= marks  && marks <= 79) {
//   console.log("B+");
// } else if (80 <= marks  && marks <= 100) {
//   console.log("A+");
// } else {
//   console.log("enter the valid number ");
// }

// var marks = Number(prompt("Enter the marks : "))
// marks = 101

// if (80 <= marks && marks <= 100) {
//   console.log("first class");
// } else if (60 <= marks && marks <= 79) {
//   console.log("second class");
// } else if (35 <= marks && marks <= 59) {
//   console.log("third class");
// } else if (0 <= marks && marks <= 34) {
//   console.log("fail");
// } else {
//   console.log("invalid input");
// }









