<?php

$t = (int)fgets(STDIN);
while ($t-- > 0) {
    $n = (int)fgets(STDIN);
    echo ($n * ($n+1) * pow(2, $n-2))."\n";
}
