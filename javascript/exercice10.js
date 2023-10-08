// afficher le prix final sachant que les taxe sont a 20%
// la reduction est de 15% si le prix TTC est de plus de 200euros
function price(nbr1){
    let prixHt = nbr1;
    let pourcentageTaxe = 20;
    let pourcentageReduction = 15;

    let taxe = (pourcentageTaxe/100)*prixHt;
    let prixTTC = prixHt + taxe
    if(prixTTC > 200){
        let reduction = (pourcentageReduction/100)*prixTTC
        let prixFinal = prixTTC - reduction
        console.log(prixFinal) 
    }else{
        console.log(prixTTC)
    }
}

price(180)