const fruits = ['vashli', 'banani', 'atami'];

for (const fruit of fruits) {
    console.log(fruit);
}

let i = 10;

while (i >= 1) {
    console.log(i);
    i--;
}

const numbers = [2, 4, 6, 8];
let sum = 0;
let index = 0;

do {
    sum += numbers[index];
    index++;
} while (index < numbers.length);

console.log("ჯამი:", sum); 