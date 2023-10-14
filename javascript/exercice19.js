// bubble sort

let array = [100,87,6,20,985,48,614,235,83,74,91,9, 2547, 69, 1647, 2596, 762, 1684, 96, 30, 7, 0, 6845]

function bubbleSort(value){
    let count = 0;
    while(count <= array.length){
        if(array[count] > array[count + 1]){
            let tampon = array[count];
            array[count] = array[count+1];
            array[count+1] = tampon;
            count = 0
        }else{
            count +=1
        }
    }
    console.log(value)
}
bubbleSort(array)