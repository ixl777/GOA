function changeElements() {
    const inputElement = document.getElementById('myInput');
    const buttonElement = document.getElementById('myButton');
    const titleElement = document.getElementById('myTitle');
    const bodyElement = document.body; 
    const inputValue = inputElement.value;
    console.log("Input-ის მნიშვნელობა:", inputValue);
    buttonElement.style.backgroundColor = 'black';
    buttonElement.style.color = 'white';
    titleElement.style.textAlign = 'center';
    bodyElement.style.backgroundColor = 'green';
}
window.onload = changeElements;

