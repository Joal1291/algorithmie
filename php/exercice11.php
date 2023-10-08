// photocopie vaut 0.25 cents, valable pour les 10 premieres
// photocopie vaut 0.20 cents, valable entre la 11eme est la 20eme
// au dela une photocopie vaut 0.10 cents 
// calculer la facure en fonction du nombre entrer 
 
<?php

function facture(int $nbr){
    $result = 0;
    $i = 1;
    while($i <= $nbr){
        if($i <= 10){$result += 0.25;}
        else if($i > 10 && $i <= 20){$result += 0.20;}
        else{$result += 0.10;}
        $i++;
    }
    echo "Le prix est de ".$result." euros";
}

?>