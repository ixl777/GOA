function submitForm(event) {
  event.preventDefault(); 

  const nameInput = document.getElementById("name");
  const nameValue = nameInput.value;
  console.log("შეყვანილი სახელი:", nameValue);
}
