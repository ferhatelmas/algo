<?php

while(true)
    foreach(explode(' ', trim(fgets(STDIN))) as $n)
        if($n === '-1') exit();
        elseif(intval($n) % 2 == 0) echo "$n\n";
