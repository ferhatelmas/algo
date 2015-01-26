<?php

$t = (int)trim(fgets(STDIN));

while ($t-- > 0) {
    echo implode(
        ' ',
        array_reverse(
            explode(
                ' ',
                trim(fgets(STDIN))
            )
        )
    )."\n";
}
