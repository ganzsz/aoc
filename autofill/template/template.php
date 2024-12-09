<?php
require_once "../utils.php";

$lines = file('input.test');

foreach ($lines as $line_num => $line) {
  echo $line . '<br>';
}
