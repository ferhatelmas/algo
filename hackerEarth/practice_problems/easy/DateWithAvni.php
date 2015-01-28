<?php

$t = (int)trim(fgets(STDIN));

while ($t-- > 0) {
    $p = null;
    $b = true;
    foreach (str_split(trim(fgets(STDIN))) as $v) {
        if ($v === $p) {
            $b = false;
            break;
        }
        $p = $v;
    }
    echo ($b ? 'KISS' : 'SLAP')."\n";
}
