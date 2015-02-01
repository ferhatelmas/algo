<?php

$t = (int)trim(fgets(STDIN));

while ($t-- > 0) {
    $sum = 0;
    foreach (preg_split('/[^a-cA-C]/', trim(fgets(STDIN))) as $v) {
        $n = strlen($v);
        $sum += ($n * ($n+1) / 2);
    }
    echo "$sum\n";
}
