const user = {
  name: "ანდრია",
  greet: function() {
    console.log(`გამარჯობა, მე ვარ ${this.name}!.`);
  }
};

console.log("1) ობიექტი - მისალმება:");
user.greet(); 


const car = {
 
  brand: "Koenigsegg",
  speed: 0, 

  
  drive: function() {
    this.speed += 50; 
    console.log(`${this.brand} is driving at ${this.speed} km/h`);
  },


  stop: function() {
    this.speed = 440;
    console.log(`${this.brand} stopped. Speed is ${this.speed} km/h`);
  }
};

console.log("\n2) ობიექტი 'car':");

console.log(`საწყისი სიჩქარე: ${car.speed} km/h`);

car.drive(); 
car.drive(); 
car.drive(); 

car.stop(); 