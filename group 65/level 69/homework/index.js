/*
   do...while ლუპი არის საკონტროლო სტრუქტურა JavaScript-ში,
   რომელიც ასრულებს კოდის ბლოკს ერთხელ მაინც, განურჩევლად იმისა,
   არის თუ არა საწყისი პირობა ჭეშმარიტი.
   შემდეგ, ის ამოწმებს პირობას (while-ში). თუ პირობა ჭეშმარიტია,
   ლუპი მეორდება. თუ პირობა მცდარია, ლუპი ჩერდება.

   სინტაქსი:
   do {
     // კოდის ბლოკი, რომელიც შესრულდება მინიმუმ ერთხელ
   } while (პირობა);
*/

/*
2) რა განსხვავებაა ჩვეულებრი while loop-სა და do while loop-ს შორის?
*/

/*
   ძირითადი განსხვავება:
   - while ლუპი: პირველად ამოწმებს პირობას და მხოლოდ ამის შემდეგ ასრულებს კოდის ბლოკს.
     თუ საწყისი პირობა მცდარია, კოდის ბლოკი არასოდეს შესრულდება. (Pre-test loop)

   - do...while ლუპი: ჯერ ასრულებს კოდის ბლოკს მინიმუმ ერთხელ, შემდეგ ამოწმებს პირობას.
     კოდის ბლოკი შესრულდება მინიმუმ ერთხელ მაინც, მაშინაც კი, თუ პირობა საწყის ეტაპზე მცდარია. (Post-test loop)
*/
console.log("3) რიცხვები 1-დან 5-მდე do...while-ით:");
let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 5);
console.log("\n4) რიცხვები 10-დან 1-მდე do...while-ით:");
let j = 10;
do {
  console.log(j);
  j--;
} while (j >= 1);
console.log("\n5) რიცხვები 1-დან მომხმარებლის მიერ შეყვანილ რიცხვამდე do...while-ით:");
let userNumber = 5;
console.log(`(ვთვლით, რომ მომხმარებელმა შეიყვანა ${userNumber})`);

if (!isNaN(userNumber) && userNumber > 0) {
  let k = 1;
  do {
    console.log(k);
    k++;
  } while (k <= userNumber);
} else {
}
console.log("\n6) ლუწი რიცხვები 1-დან 20-მდე do...while-ით:");
let l = 1;
do {
  if (l % 2 === 0) { 
    console.log(l);
  }
  l++;
} while (l <= 20);
console.log("\n7) მომხმარებლის შეყვანის შეჩერება უარყოფითი რიცხვის შეყვანამდე (ემულაცია):");
let inputNumber;
let iteration = 1;

do {
    let simulatedInputs = [10, 5, 0, -1]; 
  inputNumber = simulatedInputs.shift();

  if (inputNumber !== undefined) {
    console.log(`შეყვანილი რიცხვი: ${inputNumber}`);
    if (inputNumber >= 0) {
    } else {
      console.log("უარყოფითი რიცხვია.");
    }
  } else {
    inputNumber = -1; 
  }
  iteration++;
} while (inputNumber >= 0);
const greet = () => "Hello, World!";
console.log("\n8) Arrow function - Hello, World!:", greet());
const sum = (a, b) => a + b;
console.log("9) Arrow function - ჯამი (5 + 3):", sum(5, 3));
const checkEvenOdd = (num) => (num % 2 === 0 ? "Even" : "Odd");
console.log("10) Arrow function - ლუწი/კენტი (4):", checkEvenOdd(4));
console.log("10) Arrow function - ლუწი/კენტი (7):", checkEvenOdd(7));
/*
   Template Literals (ასევე ცნობილი როგორც Template Strings) არის ბექტიკებით (``) შემოფარგლული სტრინგები JavaScript-ში,
   რომლებიც საშუალებას იძლევა:
   1. Multi-line Strings: ტექსტის რამდენიმე ხაზზე განთავსება ახალი ხაზის სიმბოლოების (\n) გამოყენების გარეშე.
   2. String Interpolation: ცვლადების ან გამოსახულებების ჩასმას სტრინგში ${expression} სინტაქსის გამოყენებით,
      რაც ბევრად უფრო მარტივი და წასაკითხია, ვიდრე სტრინგების კონკატენაცია (+) ოპერატორით.
*/
const name = "დანიელი";
const age = 30;
console.log("\n12) Template Literals (name, age):");
console.log(`My name is ${name} and I am ${age} years old.`);


const myName = "ანდრია";
const profession = "პროგრამისტი";
const country = "საქართველო";
console.log("\n13) Template Literals (Template Sentence):");
console.log(`My name is ${myName}, I am a ${profession} from ${country}.`);

const formatPurchase = (item, price, quantity) => {
  return `You bought ${quantity} ${item}(s) for a total of ${price * quantity} GEL.`;
};
console.log("\n14) Template Literals (Function Output):");
console.log(formatPurchase("Apple", 2.5, 4)); 
/*
   Function Expression არის JavaScript-ში ფუნქციის შექმნის ერთ-ერთი გზა,
   როდესაც ფუნქცია განისაზღვრება როგორც ცვლადის მნიშვნელობა.
   ის შეიძლება იყოს ანონიმური (სახელის გარეშე) ან სახელდებული.

   მაგალითი:
   const myFunction = function(params) { ... };

   Function Declaration-ისგან განსხვავებით (რომელიც იწყება function საკვანძო სიტყვით და არ ენიჭება ცვლადს),
   Function Expression არ ექვემდებარება hoisting-ს, რაც ნიშნავს, რომ მისი გამოძახება შეიძლება
   მხოლოდ მას შემდეგ, რაც კოდში მას მივაღწევთ (ანუ, განსაზღვრის შემდეგ).
*/
const greetUser = function (userName) {
  console.log(`\n16) Function Expression - მისალმება: Hello, ${userName}!`);
};
greetUser("andria");
const calculateSum = function (num1, num2) {
  console.log(`\n17) Function Expression - ჯამი (${num1} + ${num2}): The sum is ${num1 + num2}`);
};
calculateSum(10, 7);