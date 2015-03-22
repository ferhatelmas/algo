<?php

$t = (int)fgets(STDIN);

while ($t-- > 0) {
    $n = fgets(STDIN);
    if (strpos($n, '21') > -1 or ((int)$n) % 21 == 0) {
        echo "The streak is broken!\n";
    } else {
        echo "The streak lives still in our heart!\n";
    }
}
