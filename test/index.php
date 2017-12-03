<?php
  require_once dirname(__FILE__).'/../dist/pie-gen-php/lib/php/Boot.class.php';
  echo PieChartGen::create([10, 20], [
    'innerRadiusSize' => 0.2,
    'colors' => array('#451156', '#526712')
  ]);
?>
