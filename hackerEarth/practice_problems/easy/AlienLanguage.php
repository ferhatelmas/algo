<?php

function isSub($s, $p)
{
    $c = array_fill_keys(range('a', 'z'), 0);
    foreach (str_split($s) as $e) {
        $c[$e]++;
    }

    foreach (str_split($p) as $e) {
        if ($c[$e] > 0) {
            return true;
        }
    }
    return false;
}

$t = (int)fgets(STDIN);

while ($t-- > 0) {
    echo (isSub(trim(fgets(STDIN)), trim(fgets(STDIN))) ? 'YES' : 'NO')."\n";
}
