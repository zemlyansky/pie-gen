<?php
  require_once dirname(__FILE__).'/../dist/pie-gen-php/lib/php/Boot.class.php';
?>

<div style="width: 50%">
<?= PieChartGen::create([10, 20], [
    'innerRadiusSize' => 0.9,
    'colors' => ['#451156', '#526712']
  ]);
?>
</div>
