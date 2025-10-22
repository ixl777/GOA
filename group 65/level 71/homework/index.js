/**
 * 1) რა არის DOM (კომენტარების სახით)
 * * DOM (Document Object Model) არის პროგრამირების ინტერფეისი (API) HTML და XML 
 * * დოკუმენტებისთვის. ის წარმოადგენს ვებ-გვერდს ხისებრი სტრუქტურის სახით სადაც 
 * ყველა HTML ტეგი არის "კვანძი" (Node) ან "ობიექტი" (Object).
 * * DOM-ის დახმარებით JavaScript-ს შეუძლია:
 * - ვებ-გვერდის მთელი HTML სტრუქტურის წაკითხვა შეცვლა და დამატება.
 * - HTML ელემენტებზე სტილის შეცვლა.
 * - ახალი ელემენტების შექმნა, წაშლა ან გადაადგილება.
 * - გვერდზე მომხმარებლის მოქმედებებზე (დაწკაპუნება კლავიშის დაჭერა) რეაგირება.
 */
/**
 * ძირითადი DOM მეთოდები (რაც ამ გაკვეთილებზე ვისწავლეთ/გამოვიყენეთ):
 * * I. ელემენტების წამოღება (Selector Methods):
 * ----------------------------------------
 * * 1. document.getElementById('id-name')
 * - აკეთებს: წამოიღებს *ერთ* ელემენტს მისი უნიკალური ID ატრიბუტით.
 * - აბრუნებს: ერთ Element Object-ს, ან null-ს თუ ვერ იპოვა.
 * * 2. document.getElementsByClassName('class-name')
 * - აკეთებს: წამოიღებს *ყველა* ელემენტს მოცემული კლასის სახელით.
 * - აბრუნებს: HTMLCollection-ს (ელემენტების მსგავსი მასივი).
 * * 3. document.querySelector('CSS-selector')
 * - აკეთებს: წამოიღებს *პირველ* ელემენტს, რომელიც ემთხვევა მოცემულ CSS სელექტორს (#id, .class, tag).
 * - აბრუნებს: ერთ Element Object-ს, ან null-ს.
 * * 4. document.querySelectorAll('CSS-selector')
 * - აკეთებს: წამოიღებს *ყველა* ელემენტს, რომელიც ემთხვევა მოცემულ CSS სელექტორს.
 * - აბრუნებს: NodeList-ს (forEach ციკლის გამოყენება მარტივია).
 * * II. შიგთავსის და ატრიბუტების შეცვლა (Properties/Methods):
 * --------------------------------------------------------
 * * 5. element.innerText
 * - აკეთებს: ელემენტის შიგნით არსებული მხოლოდ ტექსტის წაკითხვას ან შეცვლას (HTML ტეგების იგნორირებით).
 * * 6. element.innerHTML
 * - აკეთებს: ელემენტის შიგნით არსებული სრული შიგთავსის (ტექსტი + HTML ტეგები) წაკითხვას ან შეცვლას.
 * * 7. element.style.propertyName
 * - აკეთებს: ელემენტისთვის ინლაინ (inline) CSS სტილის მინიჭებას ან წაკითხვას (მაგ: element.style.color = 'red').
 */
const firstParagraph = document.getElementById('first-paragraph');
firstParagraph.innerText = 'ტექსტი წარმატებით შეიცვალა JS-ით getElementById-ის გამოყენებით!';

console.log('4. პირველი პარაგრაფის ტექსტი შეიცვალა.');
const secondParagraph = document.getElementsByClassName('styled-paragraph')[0]; 
secondParagraph.style.backgroundColor = '#FFD700'; 
secondParagraph.style.color = '#333';
secondParagraph.style.fontWeight = 'bold';
secondParagraph.style.borderRadius = '5px';

console.log('5. მეორე პარაგრაფის სტილი შეიცვალა');
const mainHeading = document.querySelector('#main-heading');

mainHeading.innerText = 'H1 წამოვიღეთ querySelector()-ით!';
mainHeading.style.color = '#B10DC9';

console.log('6. H1 თეგი წამოღებულია querySelector()-ით.');
const paragraphsToStyle = document.querySelectorAll('.bulk-paragraph');

console.log('7. 5 პარაგრაფის გასტილვა:');

paragraphsToStyle.forEach((pElement, index) => {
    pElement.style.border = `2px solid #2ECC40`;
    pElement.style.padding = '8px';
    pElement.style.margin = '5px 0';
    pElement.style.backgroundColor = (index % 2 === 0) ? '#D9FFD9' : '#C3FFC3'; 
    pElement.style.color = '#155724';
    pElement.textContent = `გასტილული პარაგრაფი #${index + 1}`;
    
    console.log(`   პარაგრაფი ${index + 1} გასტილდა.`);
});