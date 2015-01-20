<?php

$tc = (int)trim(fgets(STDIN));
while($tc-- > 0) {
    $p = '';
    $r = array();
    foreach(str_split(trim(fgets(STDIN))) as $w)
        if($w !== $p)
            array_push($r, $p = $w);
    echo implode($r)."\n";
}
