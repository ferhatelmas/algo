<?php

$n = (int)trim(fgets(STDIN));

$a = array();
$b = array();

foreach ((explode(' ', trim(fgets(STDIN)))) as $v) {
    if ($v % 2 === 0) {
        $a[] = intval($v);
    } else {
        $b[] = intval($v);
    }
    // array_push($v%2 === 0 ? $a : $b, intval($v));
}

sort($a);
echo implode(' ', $a)."\n";

rsort($b);
echo implode(' ', $b)."\n";
