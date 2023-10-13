// ecrire la function de index of sans celle ci

let array = ["indexof", "sans", "la", "function", "elle", "même", "provenir", "devoir", "continent"]

function indexof(value){
    for(let i = 0; i < array.length; i++){
        if(value == array[i]){
            console.log(i)
            return
        }
    }
}

indexof('indexof')