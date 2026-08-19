function add(a, b) {
    return a + b;
}
console.log(add(10, 20));

console.log("Hello, World!");


let studentname = "John Doe";
let studentage = 20;
let course = "Java Script";

console.log("Student Name: " + studentname);
console.log("Student Age: " + studentage);
console.log("Course: " + course);

let students = "john"
let age = 20
let isstudent = true
let salary = null
let address = undefined

console.log(typeof students)
console.log(typeof age)
console.log(typeof isstudent)
console.log(typeof salary)
console.log(typeof address)

let a = 10;
let b = 5;

console.log(a + b)
console.log(a - b)
console.log(a * b)

let age = 20;

console.log(age > 18);
console.log(age < 18);
console.log(age == 20);
console.log(age == 20);
console.log(age != 20);


let age = 20;

if (age >= 18) {
    console.log("You are eligible to vote.");
} else {
    console.log("You are not eligible to vote.");
}

let marks = 85;

if (marks >= 90) {
    console.log("Grade: A+");
} else if (marks >= 80) {
    console.log("Grade: A");
} else if (marks >= 70) {
    console.log("Grade: B+");
} else if (marks >= 60) {
    console.log("Grade: B");
} else {
    console.log("Grade: C");
}


let title = document.getElementById("title");
let button = document.getElementById("button");
button.addEventListener("click", function () {
    title.innerText = "Button Clicked!";
});

document.querySelector("#button")
document.addEventListener("click", function () {
    alert("Document Clicked!");
})