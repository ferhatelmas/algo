<?php

$t = (int)fgets(STDIN);
$pass = array();
while($t-- > 0) {
    $p = trim(fgets(STDIN));
    $r = strrev($p);
    if(array_key_exists($r, $pass)) {
        $c = strlen($p);
        echo"$c ".($p[(int)($c/2)])."\n";
        break;
    }
    $pass[$p] = true;
}
