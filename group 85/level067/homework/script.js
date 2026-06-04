/**Binary Search: მუშაობს მხოლოდ დალაგებულ მასივში ყოფს სიას შუაზე და ამოწმებს საძიებო რიცხვი შუაშია მარცხნივ თუ მარჯვნივ ამით ძებნის არეალი ყოველ ნაბიჯზე ნახევრდება რაც ძალიან სწრაფია

Linear Search: ამოწმებს სიის ყველა ელემენტს თანმიმდევრობით თავიდან ბოლომდე სანამ არ იპოვის სასურველს ეს მეთოდი ნელია რადგან ყოველ ელემენტს სათითაოდ გადის

Factory Function: ფუნქცია რომელიც ქმნის და აბრუნებს ობიექტებს ამარტივებს კოდს და გამორიცხავს ერთნაირი სტრუქტურის ხელახლა წერას */

function createItem(name, type, value) {
  return { name, type, value }
}
const item = createItem("Sword", "Weapon", 100)

class Bot {
  constructor(id, health, speed) {
    this.id = id
    this.health = health
    this.speed = speed
  }
  takeDamage(dmg) {
    this.health -= dmg
  }
  run(spd) {
    this.speed += spd
  }
}
