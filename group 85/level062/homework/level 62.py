class Person:
    def __init__(self, name, surname, age, birth_date):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = birth_date

    def aging(self):
        self.age += 1
        print(f"{self.name} gaxda {self.age} wlis.")
    def toString(self):
        return f"{self.name} {self.surname} daibada {self.birth_date} da aris {self.age} wlis."


p1 = Person("andria", "gobejishvili", 15, "2010-12-10")

print(p1.toString()) 

p1.aging()           
print(p1.toString())


class Warehouse:
    def __init__(self, name, category, company, status, stock, reserved=0):
        self.name = name
        self.category = category
        self.company = company
        self.status = status
        self.stock = stock
        self.reserved = reserved

    def update_status(self):
        if self.stock <= 0:
            self.status = "out-of-stock"
        elif self.stock < 5:
            self.status = "low-stock"
        else:
            self.status = "active"

    def restock(self, amount):
        self.stock += amount
        self.update_status()
        print(f"maragi ganaxlda. axali raodenoba: {self.stock}")

    def reserve(self, amount):
        if amount > self.stock:
            return False
        self.reserved += amount
        return self.reserved

    def available(self):
        return self.stock - self.reserved

    def to_string(self):
        return f"saxeli: {self.name}, xelmisawvdomi: {self.available()}, statusi: {self.status}"
    

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = {}
        self.n_id = 1

    def add_book(self, title, author, year):
        book = {
            "id": self.n_id,
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)
        self.n_id += 1
        print("wigni daemata")

    def find_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                print(book)
                return book
        return None

    def borrow_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            if book_id in self.borrowed:
                print("wigni ukve agebulia")
            else:
                self.borrowed[book_id] = True
                print("wigni agebulia")
        else:
            print("wigni ver ipoves")