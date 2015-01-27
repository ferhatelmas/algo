<?php

while (false !== ($ln = fgets(STDIN))) {
    $arr = explode('//', $ln);
    echo implode(
        '//',
        array_merge(
            array(str_replace('->', '.', $arr[0])),
            array_slice($arr, 1)
        )
    );
}
