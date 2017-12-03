<?php

class PieChartGen {
	public function __construct(){}
	static $SIZE = 302;
	static $RADIUS = 150;
	static function calculateArcs($values) {
		$a = 100;
		$ds = (new _hx_array(array()));
		$oldX = 151. + 150 * Math::cos(Math::$PI / 2);
		$oldY = 151. - 150 * Math::sin(Math::$PI / 2);
		$totalAngle = 0;
		{
			$_g = 0;
			while($_g < $values->length) {
				$v = $values[$_g];
				++$_g;
				$angle = 2 * Math::$PI * $v / 100;
				$totalAngle = $totalAngle + $angle;
				$newX = 151. + 150 * Math::cos($totalAngle - Math::$PI / 2);
				$newY = 151. + 150 * Math::sin($totalAngle - Math::$PI / 2);
				$ds->push("M " . _hx_string_rec($oldX, "") . " " . _hx_string_rec($oldY, "") . " A " . _hx_string_rec(150, "") . " " . _hx_string_rec(150, "") . " 0 " . _hx_string_rec(((($angle < Math::$PI) ? 0 : 1)), "") . " 1 " . _hx_string_rec($newX, "") . " " . _hx_string_rec($newY, "") . " L " . _hx_string_rec(151., "") . " " . _hx_string_rec(151., "") . " Z");
				$oldX = $newX;
				$oldY = $newY;
				unset($v,$newY,$newX,$angle);
			}
		}
		return $ds;
	}
	static function run($arr) {
		{
			$a = $arr;
			$arr = new _hx_array($a);
		}
		return _hx_len($arr);
	}
	function __toString() { return 'PieChartGen'; }
}
