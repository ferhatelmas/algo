<?php

while(($i = (int)+fgets(STDIN)) !== -1)
    if($i%2 === 0)
        echo $i."\n";