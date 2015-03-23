<?php

fgets(STDIN);

$n = 0;
foreach (explode(' ', fgets(STDIN)) as $v) {
    if (floatval($v) < 300000000) {
        $n++;
    }
}
echo "$n\n";
