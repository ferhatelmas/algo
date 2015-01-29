<?php

$arr = explode(' ', trim(fgets(STDIN)));

$i = $sum = 0;
while ($i < $arr[0]) {
    if ($i%$arr[1] === 0 or $i%$arr[2] === 0) {
        $sum += $i;
    }
    $i++;
}

echo "$sum\n";
