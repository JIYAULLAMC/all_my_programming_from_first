
// use of backtic 
// difference between `` "" ''
// difference between let var const
// console.log(`My hobbies are :
// 1 : reading,
// 2 : writing,
// 3 : sleeping,
// `)

// var  a = 10;
// var  b = 20;
// console.log("addition of "+ a +" and "+ b+ " is", a+b)
// console.log("addition of", a ,"and",b, "is", a+b)
// console.log(`addition of ${a} and ${b} is ${a+b}`)

// data types : deals about the type of kind of data
// any mathematical number in js is considers as number data type example 0.1, 1, 1.0, 110
// string anyting which is enclosed with single and double quotes and backtick is called as string data type
// `` backtick, interpolation, template string is backtick is introduced in es6 and advantages of
// using backtick is
// 1) we can enclose single quotes and double quotes
// 2) we can write more than one line (multiple line) known as template string
// 3) backtick used to variables, evaluate the expressiong using backtick using ${variable and expression}

// when we want to check the condition we make use of boolean data type
// that are true and false value are 1 and 0
// true and false are keywords in js keyword should always be in lowercase
// var a = true
// // var c = True  not valid
// console.log(a)
// console.log(Number(a))

// var b = false
// console.log(b)
// console.log(Number(b))

// var a;  //declaration
// var a = undefined;
// var undefined= 10 // undefined is keyword
// //when we are declaring variable but not initializing a value to it then the resultant will be undefined

// var a = prompt()

// insted of storing the data undefined we can make use of data type null
// type of null is an object

// console.log(typeof " done with file structure") //  it is String
// console.log( typeof `done with file structure `) //  it is string
// console.log( typeof 'done with file structue' ) // it is String
// console.log( typof(47) )   // number



// array is used to store the multiple values it accecpt heterogeneous values
// the collection of heterogeneous value is known as array
// heterogeneous value means it accepts all kind of data types

// the below is syntax for creating an array
// var a = [1,2,3,4]
// console.log(a,)

// var a = [1,2.0, 0.2]
// console.log(a,)

//     var a = [1, "abc", true, false, undefined, null]
//     console.log(a,)

// var a = [1, "abc", true, false, undefined, null]
// console.log(a.length)
// document.write(a)
// console.log(a.length)



// 6
// demo2.js:66 6
// a
// (6) [1, 'abc', true, false, undefined, null]0: 11: "abc"2: true3: false4: undefined5: nulllength: 6[[Prototype]]: Array(0)
// console.log(a[1])
// VM5764:1 abc
// undefined
// console.log(a[0])
// VM5834:1 1
// undefined
// console.log(a[9])
// VM5875:1 undefined
// undefined
// console.log(a[10])
// VM5901:1 undefined
// undefined
// console.log(a[4])
// VM5928:1 undefined
// undefined
// console.log(a[10])
// VM5951:1 undefined
// undefined
// document.write(a)
// undefined
// document.write(a[0])
// undefined
// document.write(a[5])
// undefined
// document.write(a[a.length]-1)
// undefined
// document.write(a[a.length-1])

// var a = [1, "abc", true, false, undefined, null];
// aa = {
//     'a' : a,
//     'aaa':123,
// }
// let b = [1, "abc", true, false, undefined, null];

// bb = {
//     'b':b,
//     'bbb':123,
// }



// i = 5
// a = i-- + i--
// console.log(a,i)

// create an array the value in array should be any string or number data type the length should be 5
// access the each value of an array
// var arr = ["aaa", "bbb",12,"ddd",345]
// console.log(arr[0])
// console.log(arr[1])
// console.log(arr[2])
// console.log(arr[3])
// console.log(arr[4])
// reassign the third index value
// arr[3]="67787"
// console.log(arr)
// access the last of value
// console.log(arr[arr.length-1])

// ---------------------------------------------

// var arr = [1,4,'aaaa', 3434]
// //  how to add and remove the elements to and from the array at last index
// console.log("the original array",arr)
// // how to add the element at the last 
// arr.push(true)
// console.log("array after adding ->",arr[arr.length-1],"->",arr)

// // how to remove the element from the last index
// arr.pop()
// console.log("array after removing ->",arr[arr.length-1],"->",arr)

// // ---------------------------------------------
// //  how to add and remove the elements to and from the array at first index
// // how to remove the elements from the first index
// console.log("the original array",arr)
// arr.shift()
// console.log("the  array after removing",arr)
// // how to add the elements from the first index
// arr.unshift("mala")
// console.log("the  array after adding",arr)

// // how to reverse the array of elements
// var arr = ["aaa", "bbb",12,"ddd",345]
// console.log("before reversing",arr)
// console.log("before reversing", arr.reverse())

// var arr = ["aaa", "bbb",12,"ddd",345]

// // how to find the index of any value present in list
// console.log(arr.indexOf("bbb"))
// var arr = ["aaa", "bbb",12,"ddd",345]

// // how to find the index of any value which is not present in list -> it will give -1
// console.log(arr.indexOf("zzz"))
// var str = "abc"


// var arr = ["aaa", "bbb",12,"ddd",345]
// console.log("aaa is present in array",arr.includes("aaa"));
// console.log("yyy is present in array",arr.includes("yyy"));


// how to join anything inbetween the element in  

// var a = [10, 20, 30]

// console.log(a.join("->*"))


// console.log("------------------------------------")
// var name = "JiyAullA M chindAdi"

// console.log(name.toUpperCase())
// console.log(name.toLowerCase())

// var a = 10
// var b = '20'

// console.log(a+b);
// console.log(b.concat(a));
// console.log(a.concat(b));


// how to add the two are more array
// var aa = 10
// var a = [1,2,3, "abc"]
// var b = ["a", "b", 23.39, ]
// console.log(a.concat(b));
// console.log(b.concat(a));
// console.log(a.concat(a));
// console.log(b.concat(b));
// console.log(a.concat(aa));


// var name = "          Vishwanatha       "
// var res = name.trim()

// console.log(res);


// var name = "karthik"
// var arr_name = name.split("")
// rev_arr_name = arr_name.reverse()
// out_name = rev_arr_name.join("")
// console.log(out_name);

// console.log("jiya".split('').reverse().join(""));

// var  name = "malala"
// // used to find the last index of occuring charecter

// console.log(name.lastIndexOf("m"));
// console.log(name.lastIndexOf("l"));
// console.log(name.lastIndexOf("o"));

// //help to find whetherr the string is ending with charecter or not
// console.log(name.endsWith("a"))
// console.log(name.endsWith("l"))


// console.log(4 + "1")

