document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('task-1').innerHTML = "Hello World!";

    document.querySelector('#task-2').innerHTML = "<h2>ეს არის H2 სათაური</h2>";

    document.getElementsByClassName('task-3')[0].innerHTML = "<p>This is a paragraph</p>";

    document.querySelector('#task-4').innerHTML = `
        <h3>ახალი სტრუქტურა</h3>
        <ul>
            <li>andria</li>
            <li>dani</li>
        </ul>
    `;

    document.getElementById('task-5').innerHTML = '<img src="https://via.placeholder.com/300x100" alt="Sample Image">';
    document.querySelector('#task-6').innerHTML += " <strong>და ესეც დამატებული ტექსტი!</strong>";
    document.getElementById('task-7').innerHTML = "New content updated!";
    document.querySelector('#task-8').innerHTML = `
        <div>
            <h4>ეს არის ბლოკი Main-ში</h4>
            <p>რამდენიმე ტექსტური პარაგრაფი რომელიც დაემატა innerHTML-ით</p>
        </div>
        <p>კიდევ ერთი პარაგრაფი</p>
    `;

});