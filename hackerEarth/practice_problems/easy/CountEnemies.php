<?php

$t = (int)trim(fgets(STDIN));

while ($t-- > 0) {
    $c = 0;
    foreach (explode('*', trim(fgets(STDIN))) as $ln) {
        $arr = str_split($ln);
        if (count(array_unique($arr)) == 1 and $arr[0] == 'O') {
            $c += count($arr);
        }
    }
    echo "$c\n";
}
