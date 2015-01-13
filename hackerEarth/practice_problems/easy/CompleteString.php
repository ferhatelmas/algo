<?php

$k = (int)+fgets(STDIN);
for($i=0; $i<$k; $i++) {
    $w = array();
    foreach(str_split(trim(fgets(STDIN))) as $_ => $c)
        if(!array_key_exists($c, $w))
            $w[$c] = true;
    echo (count($w) === 26 ? "YES" : "NO")."\n";
}
