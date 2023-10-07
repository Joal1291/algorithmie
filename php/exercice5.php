ecrire un algo qui permet d'afficher le plus grand des trois nombre saisie au clavie
<?php
function wichOneHigher(int $nbr1, int $nbr2, int $nbr3){
    $nbrtoreturn = "";
    $array = [$nbr1, $nbr2, $nbr3];

    for($i = 0; $i < count($array); $i++){
        if($array[$i] === $array[0]){
            $nbrtoreturn = $array[$i];
        }else{
            if($array[$i] > $nbrtoreturn){
                $nbrtoreturn = $array[$i];
            }
        }
    }
    echo "Le plus grand nombre est : $nbrtoreturn\n";
}
?>