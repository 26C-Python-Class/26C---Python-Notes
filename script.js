const numbers = 123// int
let dero = [true, false, 1, 3, 5, "Derrick"]// array
// boolean - true or false
obj = {}
let unknown 
console.log(unknown)
console.log('')
let num = "jose"
myName = parseInt(num)
console.log(myName)

let a = 5
let b = 7
console.log(a == b)
// operators + - / *
console.log(b % a)
 // string concatenation / interpolation
 let name = "Derrick"
 let my_name = `Derrick
 Watako`
 let greeting = "Hello "
 console.log('Hello '  + name)// concatenation
 console.log(`Hello ${name}`)// interpolation
 console.log(greeting.concat(name))
 let programming = ["JavaScript", "Python", "Java", "C", "C#"]
 x = programming.join(', ')
 console.log(x)

 let count;
 for (let count = 0; count < 10; count ++ ) {
    console.log(count)
 }

 // Comparison operators
 a == b // comparison loose
 a === b
//  <= less than or equal to
// >= greater than or equal to

let age = 19;

if (age >= 18) {
    console.log("You are eligible to vote")
} else if (age >= 7) {
    console.log("Go to school and read")
} else {
    console.log("You are a toddler! Go get breast milk")
}

// Ternary operator
let vote = (age >= 18) ? "You are eligible to vote" : "Go to school and read"
console.log(vote)

    
    
    // // Theme Toggle
    //     const themeBtn = document.getElementById('theme-toggle');
    //     themeBtn.addEventListener('click', () => {
    //         document.body.classList.toggle('dark-theme');
    //     });

    //     // Form Submission Interaction
    //     document.getElementById('contactForm').addEventListener('submit', (e) => {
    //         e.preventDefault();
    //         const btn = e.target.querySelector('button');
    //         btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> TRANSMITTING...';
    //         setTimeout(() => {
    //             btn.innerHTML = '<i class="fa-solid fa-check"></i> MESSAGE DEPLOYED';
    //             btn.style.background = "#2ecc71";
    //             e.target.reset();
    //         }, 2000);
    //     });