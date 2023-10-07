function display(nbr1, nbr2){
    let displayres = nbr1 * nbr2
    if(nbr1 == 0 || nbr2 == 0){
        console.log('Le résultat est nul')
    }else if(displayres < 0){
        console.log('Le produit est négatif: ', displayres)
    }else{console.log('Le produit est postif:', displayres)}
}
display(0, 10)