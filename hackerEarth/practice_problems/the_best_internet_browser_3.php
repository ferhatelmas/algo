<?php

for($i=0, $k=trim(fgets(STDIN)); $i<$k; $i++) {
    $s = trim(fgets(STDIN));
    $l = strlen($s);
    $c = 4;
    for($j=4; $j<$l-4; $j++)
        if(strstr("aeiou", $s[$j]) === False) $c++;
    echo $c."/".$l."\n";
}
