<?php

$t = (int)trim(fgets(STDIN));

$c = 0;
while ($t-- > 0) {
    $k = (int)trim(fgets(STDIN));
    if ($k % 3 === 0) {
        $c++;
    }
}

echo "$c\n";
