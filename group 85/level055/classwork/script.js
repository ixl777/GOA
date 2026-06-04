const numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const checkParity = numbers1.map(num => num % 2 === 0);
console.log(checkParity); 

const numbers2 = [5, 12, 7, 20, 3, 8];
const checkSize = numbers2.map(num => num > 10 ? "დიდი" : "პატარა");
console.log(checkSize);
