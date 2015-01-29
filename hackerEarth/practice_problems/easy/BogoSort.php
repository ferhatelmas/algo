<?php

$t = (int)trim(fgets(STDIN));

$a = array();
while ($t-- > 0) {
    $a[] = (int)trim(fgets(STDIN));
}
sort($a);
echo implode("\n", $a)."\n";
