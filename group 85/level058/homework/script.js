function greet(name){
    console.log("hello" + name)

}

greet("andria")
greet("luka")
greet("danieli")

let sia= [2,10,-30,100,96,50,90]
function umciresi(sia) {
    let min = sia[0]
    for (let i = 1; i < sia.length; i ++)
    {
        if (sia[i] < min){
            min= sia[i]
        }
    }
    return min
}

console.log(umciresi(sia))


function luwi(num){
    if(num === 0)
        return "zero";
    else if (num % 2 !==0)
        return num **2;
    else {
        return num **3
    }
}

console.log(luwi(3))
console.log(luwi(2))
console.log(luwi(0))