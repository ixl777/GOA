let age = prompt("გთხოვთ შეიყვანოთ თქვენი ასაკი:");

if (age < 18) {
    alert("წვდომა შეზღუდულია");
} else {
    alert("წვდომა დაშვებულია");
}

let num1 = prompt("შეიყვანეთ პირველი რიცხვი:");
let num2 = prompt("შეიყვანეთ მეორე რიცხვი:");
let sum = Number(num1) + Number(num2);

alert("ამ ორი რიცხვის ჯამია: " + sum);
let price = Number(prompt("შეიყვანეთ ნივთის საწყისი ფასი:"));
let discountPercent = Number(prompt("შეიყვანეთ ფასდაკლების პროცენტი:"));

let finalPrice = price - (price * discountPercent / 100);

alert("თქვენი ნივთის ფასი ფასდაკლების შემდეგ არის: " + finalPrice + " ლარი");
