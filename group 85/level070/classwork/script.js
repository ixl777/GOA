function checkEvenOdd(number) {
  if (number % 2 === 0) {
    return "ლუწი"
  } else {
    return "კენტი"
  }
}
function findMax(numbers) {
  let max = numbers[0]
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i]
    }
  }
  return max
}