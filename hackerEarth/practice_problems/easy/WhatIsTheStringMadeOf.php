<?php

$sum = 0;
$m = array(6, 2, 5, 5, 4, 5, 6, 3, 7, 6);
foreach(str_split(trim(fgets(STDIN))) as $k => $v)
    $sum += $m[$v];
echo "$sum\n";
