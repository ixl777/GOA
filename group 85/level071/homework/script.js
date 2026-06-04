const person = {
  name: "ანდრია",
  surname: "გობეჯიშვილი",
  age: 28
}
const countries = {
  Georgia: "თბილისი",
  France: "პარიზი",
  Japan: "ტოკიო"
}
const car = {
  model: "BMW",
  engine: "3.0",
  year: 2022,
  color: "შავი"
}
car.model = "Audi"

const animals = {
  pet1: "ძაღლი",
  pet2: "კატა",
  pet3: "კურდღელი"
}
const fruits = {
  apple: 3.5,
  banana: 4.0,
  orange: 5.0
}
const pcParts = {
  cpu: "Intel Core i3 12100f",
  gpu: "Nvidia rx 6600",
  ram: "32GB"
}

const movies = {
  top1: "Inception",
  top2: "Interstellar",
  top3: "The Matrix",
  top4: "The Dark Knight",
  top5: "Pulp Fiction"
}

const user = {
  name: "ანდრია",
  sayHi() {
    console.log(`გამარჯობა, მე ვარ ${this.name}`)
  }
}

const calc = {
  num1: 10,
  num2: 20,
  result1: 0,
  result2: 0,
  plus() {
    this.result1 = this.num1 + this.num2
  },
  minus() {
    this.result2 = this.num2 - this.num1
  },
  toString() {
    console.log(`ჯამი: ${this.result1}, სხვაობა: ${this.result2}`)
  }
}

const auto = {
  model: "Toyota",
  engine: 2.0,
  horsepower: 150,
  upgrade() {
    this.engine += 2.0
    this.horsepower += 300
  },
  toString() {
    console.log(`მოდელი: ${this.model}, ძრავი: ${this.engine}, ცხენის ძალა: ${this.horsepower}`)
  }
}
