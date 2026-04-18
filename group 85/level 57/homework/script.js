for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}


const cities = ['kutaisi', 'xashuri', 'gori'];
for (const city of cities) {
    console.log(city.toUpperCase());
}

let value = 50;
while (value > 0) {
    value -= 10;
}
console.log(value); 

let num = 5;
do {
    console.log(num);
    num++;
} while (num <= 15);

const word = "vashlunia";
for (let i = 0; i < word.length; i++) {
    console.log(word[i]);
}

const fruits = ['vashli', 'atami', 'yurdzeni'];
let index = fruits.length - 1;

do {
    console.log(fruits[index]);
    index--;
} while (index >= 0);