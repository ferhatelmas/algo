<?php

$t = (int)trim(fgets(STDIN));

while ($t-- > 0) {
    $y = true;
    $s = trim(fgets(STDIN));
    foreach (str_split($s) as $e) {
        if (strstr("018", $e) === false) {
            $y = false;
            break;
        }
    }
    echo (($y && $s === strrev($s)) ? "YES" : "NO") . "\n";
}
