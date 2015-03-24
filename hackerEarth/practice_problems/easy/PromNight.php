<?php

function getArr()
{
    return array_map('intval', explode(' ', trim(fgets(STDIN))));
}

$t = (int)fgets(STDIN);

while ($t-- > 0) {
    list($m, $n) = getArr();
    $boys = getArr();
    $girls = getArr();
    sort($boys);
    sort($girls);
    $ok = true;
    foreach (array_map(null, $boys, array_slice($girls, 0, $m)) as $v) {
        if ($v[0] <= $v[1]) {
            echo "NO\n";
            $ok = false;
            break;
        }
    }
    if ($ok) {
        echo "YES\n";
    }
}
