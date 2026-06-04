const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

numbers.forEach(num => {
  if (num % 2 === 0) {
    const cube = Math.pow(num, 3);
    console.log(`რიცხვი ${num}-ის კუბი არის: ${cube}`);
  }
});
