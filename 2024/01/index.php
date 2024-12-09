<?php
require_once "../utils.php";

$lines = file('input.real');

foreach ($lines as $line_num => $line) {
  $input[$line_num] = $line;
  $items = preg_split("/ +/", $line);
  $l[] = intval($items[0]);
  $r[] = intval($items[1]);
}

sort($l);
sort($r);

$sum1 = 0;

for ($i = 0; $i < sizeof($l); $i++) {
  $dist = abs($l[$i] - $r[$i]);
  $sum1 += $dist;
}

echo "<h3>Part 1: " . $sum1 . "</h3>";

$rvals = array_count_values($r);
$lvals = array_count_values($l);
$sum2 = 0;

foreach ($lvals as $num => $count) {
  if (array_key_exists($num, $rvals)) {
    $sum2 += $count * $num * $rvals[$num];
  }
}

echo '<h3>Part 2: ' . $sum2 . '</h2>';
