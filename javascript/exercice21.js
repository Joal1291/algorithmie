// display an array with all the whole number between 1 and n integer

function isWholeNumber(n){
    if(n < 1 || n == 1 || n == 2 || n == 3){return true}
    for(let i = 2; i <= n-1;i++){
        if(n%i == 0){return false}
    }
    return true
}
function displayWholeNumberInRange(nbr){
    let array = [];
    for(let i = 1; i < nbr ; i++){
        if(isWholeNumber(i)){array.push(i); i++}
        else{i++}
    }
    array.push(nbr)
    console.log(array)
}
displayWholeNumberInRange(200)