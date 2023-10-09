// display multiplication table of 5

function multiplication(){
    let table = 5
    let multiplier = 0
    let array = []
    while(multiplier <= 10 ){
        let result = multiplier * table
        array.push(result)
        multiplier +=1
    }
    console.log(array)
}
multiplication()