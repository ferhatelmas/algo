<?php

$t = intval(fgets(STDIN));
while ($t-- > 0) {
    $r = 0;
    foreach (count_chars(trim(fgets(STDIN)), 1) as $k => $v) {
        if ($v % 2 == 1) {
            $r += 1;
        }
    }
    echo ($r > 1 ? $r - 1 : 0)."\n";
}
