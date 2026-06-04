const car = {
    brand: "Koenigsegg",
    model: "Agera R",
    year: 2014,
    color: "Snow White",
    speed: 0,

    accelerate: function() {
        this.speed += 10;
        console.log(`სიჩქარე გაიზარდა: ${this.speed} კმ/სთ`);
    },
    brake: function() {
        if (this.speed < 10) {
            this.speed = 0;
        } else {
            this.speed -= 10;
        }
        console.log(`სიჩქარე შემცირდა: ${this.speed} კმ/სთ`);
    },
    toString: function() {
        return `მანქანა ${this.brand}, ${this.model}, გამოიშვა ${this.year} წელს და არის ${this.color} ფერის`;
    }
};

car.rimType = "Aircore Hollow Carbon Fiber";
car.engineConfig = "5.0L V8 Twin-Turbo";
console.log(car.toString());
car.accelerate();          
car.brake();              
car.brake();                 