function sayHello() {
  return "Hello World"
}

function greet(name) {
  return "Hello " + name
}
function double(number) {
  return number * 2
}
function getArea(width, height) {
  return width * height
}
function isHot(temperature) {
  return temperature > 30
}
function getEven(numbers) {
  return numbers.filter(n => n % 2 === 0)
}
function checkAge(age) {
  return age < 18 ? "too young" : "come in"
}
const cat = {
  name: "მურა",
  age: 3,
  isFriendly: true
}
console.log(cat.name)
console.log(cat.age)
console.log(cat.isFriendly)
const car = {
  model: "Honda Civic",
  year: 2018
}
console.log("მე ვატარებ " + car.year + " წლის " + car.model + "-ს")
const myCar = {
  engineOn: false,
  startEngine: function() {
    this.engineOn = true
  }
}
