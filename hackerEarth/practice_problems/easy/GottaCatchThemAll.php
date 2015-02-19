<?php

fgets(STDIN);
list($r, $arr) = array(0, array_map('intval', explode(' ', fgets(STDIN))));
rsort($arr);
foreach ($arr as $k => $v) {
    $r = max(array($r, $k + $v));
}
echo ($r + 2)."\n";
