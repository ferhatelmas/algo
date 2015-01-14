<?php
function getInt() {
    return (int)+trim(fgets(STDIN));
}
$l = getInt();
$t = getInt();
while($t-- > 0) {
    $arr = explode(' ', trim(fgets(STDIN)));
    if($arr[0] < $l or $arr[1] < $l) echo "UPLOAD ANOTHER\n";
    elseif($arr[0] == $arr[1]) echo "ACCEPTED\n";
    else echo "CROP IT\n";
}
