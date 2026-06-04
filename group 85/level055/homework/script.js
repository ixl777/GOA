const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
console.log(doubled);

const ages = [10, 15, 20, 25];
ages.forEach(num => {
    console.log(num > 18 ? "yes" : "no");
});

const numbers1 = [3, 6, 9, 12];
const sum = numbers1.reduce((acc, curr) => acc + curr, 0);
console.log(sum);

const numbers2 = [2, 4, 6, 8];
numbers2.forEach(num => {
    console.log(num % 4 === 0);
});

const numbers3 = [7, 14, 21, 28];
const divided = numbers3.map(num => num / 7);
console.log(divided);

const numbers4 = [1, 3, 5, 7];
const oddCount = numbers4.filter(num => num % 2 !== 0).length;
console.log(oddCount);

const numbers5 = [2, 5, 8, 11];
numbers5.forEach(num => {
    console.log(num < 6 ? "low" : "high");
});

const numbers6 = [4, 9, 16, 25];
const roots = numbers6.map(num => Math.sqrt(num));
console.log(roots);

const numbers7 = [100, 200, 300];
const dividedByTen = numbers7.map(num => num / 10);
console.log(dividedByTen);

const numbers8 = [1, 2, 3, 4, 5];
const evens = numbers8.filter(num => num % 2 === 0);
console.log(evens);

