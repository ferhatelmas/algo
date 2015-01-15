<?php
$s = trim(fgets(STDIN));
$l = strlen($s);
$k = (int)trim(fgets(STDIN));

function index($s) {
    global $l;
    return (((int)$s)-1) % $l;
}

for($i=0; $i<$k; $i++) {
    $arr = explode(" ", fgets(STDIN));
    echo ($s[index($arr[0])] == $s[index($arr[1])] ? "Yes" : "No")."\n";
}
