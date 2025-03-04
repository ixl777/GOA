import tkinter as tk
import time
#quiz
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        #კითხვები
        self.questions = [
            {"question": "What is the capital of France?", "choices": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is 4 + 4", "choices": ["3", "4", "7", "8"], "answer": "8"},
        ]
        
        self.current_question = 0
        self.score = 0
        self.time_limit = 10  
        self.start_time = time.time()
        
        self.question_label = tk.Label(root, text=self.questions[self.current_question]["question"])
        self.question_label.pack()
            #კითხვის არჩევა
        self.choice_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            btn.pack()
            self.choice_buttons.append(btn)         #ღილაკები
        
        self.update_choices()
        self.timer_label = tk.Label(root, text="Time left: 10s")        #10 წამი ყველა კითხვაზე
        self.timer_label.pack()
        self.update_timer()
    
    def update_choices(self):
        for i, choice in enumerate(self.questions[self.current_question]["choices"]):
            self.choice_buttons[i].config(text=choice)      #კითხვების ვარიანტები
    
    def check_answer(self, choice_index):
        if self.questions[self.current_question]["choices"][choice_index] == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["question"])
            self.update_choices()
            self.start_time = time.time()
        else:
            self.question_label.config(text=f"Quiz finished! Your score: {self.score}")
            for btn in self.choice_buttons:
                btn.pack_forget()
            self.timer_label.pack_forget()
    
    def update_timer(self):
        time_left = self.time_limit - int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time left: {time_left}s")
        if time_left > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
#კალკულატორი
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":                 #მიმატება
            result = value1 + value2
        elif operator == "-":               #გამოკლება
            result = value1 - value2
        elif operator == "*":               #გამრავლება 
            result = value1* value2
        elif operator == "/":               #გაყოფა
            result = value1 / value2
        elif operator == "%":              #პროცენტულობა
            result = value1 % value2
        elif operator == "**":
            result == value1 ** value2
        elif operator == "//":
            result == value1 // value2
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        result_label.config(text=f"Result: {value1} {operator} {value2} = {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

root = tk.Tk()
root.title("calculatori proeqtistvis :)")

tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter operator:").grid(row=1, column=0)
operator_var = tk.StringVar(value="+")
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "%", "//", "**")
operator_menu.grid(row=1, column=1)

tk.Label(root, text="Enter second number:").grid(row=2, column=0)       #მეორე რიცხვი
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2) 
root.mainloop()
            #ჯეირანი
import random
play_again=True
choices=["rock", "paper", "scissors"] # ამორჩევა

#main while Cycle

while play_again == True:
    user_choice = input("Enter either rock paper or scissors: ").lower()
    while user_choice not in choices:
        print("invalid choise")
        user_choice = input("Enter either rock paper or scissors: ").lower()
    computer_choice = random.choice(choices)

    #ამორჩევა
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)



    if user_choice == computer_choice:
        print("It's a tie!")        #ფრე
    elif (user_choice == "rock" and computer_choice == "scissors"): 
        print("You win!")              #მოგება
    elif (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")              #წაგება



    stop_playing=input("do you want to spot playing?: ").lower()
    if stop_playing =="yes":
        play_again = False
        print("thanks for playing!")        #მადლობა თამაშისთვის
    elif stop_playing =="no":
        play_again = True