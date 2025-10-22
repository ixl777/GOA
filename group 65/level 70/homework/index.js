const mainTitle = document.querySelector('#main-title');
const specialDiv = document.querySelector('#special-div');
mainTitle.innerText = 'სათაური წარმატებით შეიცვალა ექსტერნალური JS-ით!';
specialDiv.style.backgroundColor = '#6200EE';
specialDiv.style.color = 'white';
specialDiv.style.borderRadius = '5px';
specialDiv.innerHTML = '<b>ID</b> ელემენტის სტილი შევცვალეთ'; 
console.log('ID ელემენტი გასტილდა.');

const colorBoxes = document.querySelectorAll('.color-box');
const colors = ['#FF4136', '#2ECC40', '#0074D9', '#FF851B']; 

console.log('\n--- სხვადასხვა ფერით გასტილვა (For Loop) ---');

for (let i = 0; i < colorBoxes.length; i++) {
    const color = colors[i % colors.length]; 
    
    colorBoxes[i].style.backgroundColor = color;
    colorBoxes[i].textContent = `ფერი #${i + 1}`;
    
    console.log(`ყუთი ${i + 1} ფერი: ${color}`);
}

const generalTexts = document.querySelectorAll('.general-text');

console.log('\n--- ყველა ტექსტის სტილის შეცვლა (forEach) ---');
generalTexts.forEach((element, index) => {
    element.style.fontWeight = '600';
    element.style.paddingLeft = '15px';
    if (index === 0) {
        element.style.borderLeftColor = '#FFDC00';
        element.style.color = '#B10DC9';
    } else {
        element.style.borderLeftColor = '#2ECC40';
        element.style.color = '#2ECC40';
    }

    element.textContent += ` - შეცვლილი`;
    console.log(`ტექსტი #${index + 1} გასტილდა`);
});