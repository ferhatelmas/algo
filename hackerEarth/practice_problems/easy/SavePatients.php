<?php

function getArray()
{
    $arr = array_map('intval', explode(' ', fgets(STDIN)));
    sort($arr);
    return $arr;
}

fgets(STDIN);
foreach (array_map(null, getArray(), getArray()) as $v) {
    if ($v[0] < $v[1]) {
        echo "No\n";
        exit(0);
    }
}
echo "Yes\n";
