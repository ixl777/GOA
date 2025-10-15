function userLoop() {
    let firstNumber = Number(prompt("შეიყვანეთ პირველი რიცხვი:"));
    let secondNumber = Number(prompt("შეიყვანეთ მეორე რიცხვი:"));

    if (isNaN(firstNumber) || isNaN(secondNumber)) {
        alert("გთხოვთ შეიყვანოთ ვალიდური რიცხვები.");
        return;
    }

    console.log("რიცხვები " + firstNumber + "-დან " + secondNumber + "-მდე:");
    if (firstNumber <= secondNumber) {
        for (let i = firstNumber; i <= secondNumber; i++) {
            console.log(i);
        }
    } else {
        for (let i = firstNumber; i >= secondNumber; i--) {
            console.log(i);
        }
    }
}

window.onload = userLoop;