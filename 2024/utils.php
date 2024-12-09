<?php
function hdump($val)
{
    echo '<pre>' . nl2br(print_r($val, true)) . '</pre>';
}
