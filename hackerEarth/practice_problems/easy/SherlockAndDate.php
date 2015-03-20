<?php

$t = (int) fgets(STDIN);
while ($t-- > 0) {
    echo date_sub(
        new DateTime(fgets(STDIN)),
        new DateInterval('P1D')
    )->format('j F Y')."\n";
}
