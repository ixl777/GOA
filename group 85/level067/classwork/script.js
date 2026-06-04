function linearSearch(arr, target) {
    for (let i in arr) {
        if (arr[i] === target) return i;
    }
    return -1;
}

const numbers = [12, 5, 78, 45, 11, 8, 34];
console.log(linearSearch(numbers, 11)); 