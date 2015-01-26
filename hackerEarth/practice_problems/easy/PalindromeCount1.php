<?php

$s = trim(fgets(STDIN));
$l = strlen($s);
$c = $l;

for ($i=$l; $i>1; $i--) {
    for ($j=0; $j<=$l-$i; $j++) {
        $ss = substr($s, $j, $i);
        if (strrev($ss) === $ss) {
            $c++;
        }
    }
}
echo "$c\n";
