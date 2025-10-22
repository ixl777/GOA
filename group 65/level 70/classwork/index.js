const firstParagraph = document.getElementById('first-paragraph');
console.log('--- 1. ელემენტი ID-ის მიხედვით ---');
console.log(firstParagraph);
const boxElements = document.getElementsByClassName('box');
const listItems = document.querySelectorAll('.list-item');
console.log('\n--- 2. ელემენტები კლასის მიხედვით (HTMLCollection) ---');
console.log(boxElements);
console.log('\n--- 3. ელემენტები querySelectorAll-ის მიხედვით (NodeList) ---');
console.log(listItems);

firstParagraph.style.backgroundColor = '#333';
firstParagraph.style.color = 'white';
firstParagraph.textContent = 'ეს აბზაცი გასტილულია JavaScript-ის დახმარებით (ID)';
for (let i = 0; i < boxElements.length; i++) {
    const box = boxElements[i];
    

    console.log(`ყუთი #${i + 1}:`, box); 
    if (i % 2 === 0) {
        box.classList.add('styled-by-js'); 
        box.textContent += ' - JS-ით შეცვლილი!';
    } else {
        box.style.border = '3px dashed purple';
    }
}


listItems.forEach((item, index) => {
    console.log(`სია #${index + 1}:`, item);
    if (index === listItems.length - 1) { 
        item.style.fontWeight = '900';
        item.style.backgroundColor = '#38c172';
        item.textContent = item.textContent.toUpperCase() + ' (ბოლო!)';
    }
});