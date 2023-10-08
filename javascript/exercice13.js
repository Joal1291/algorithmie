function whatsthemonth(nbr){
    let array = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"];

    if(nbr < 1 || nbr > 12){console.log("Invalid number")}
    else{console.log("Le mois est:", array[nbr-1])}
}
whatsthemonth(6)