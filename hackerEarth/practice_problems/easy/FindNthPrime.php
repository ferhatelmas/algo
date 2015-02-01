<?php

$k = (int)trim(fgets(STDIN));

$l = 1000000;
$s = array_fill(0, $l, true);
$r = array();

for ($i=2; $i<$l; $i++) {
    if ($s[$i]) {
        $r[] = $i;
        for ($j=$i*2; $j<$l; $j+=$i) {
            $s[$j] = false;
        }
    }
}

echo $r[$k-1]."\n";
