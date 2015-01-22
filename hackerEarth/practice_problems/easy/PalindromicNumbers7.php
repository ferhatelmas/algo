<?php

$t = (int)trim(fgets(STDIN));

while ($t-- > 0) {
    $arr = explode(' ', trim(fgets(STDIN)));
    $c = 0;
    for ($i = $arr[0]; $i <= $arr[1]; $i++) {
        $c += (strrev($i) == $i);
    }
    echo "$c\n";
}
