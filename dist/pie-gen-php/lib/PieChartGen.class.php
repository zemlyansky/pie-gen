<?php

class PieChartGen {
	public function __construct(){}
	static $SIZE = 300;
	static $RADIUS = 130;
	static function calculateArcs($values) {
		$a = 100;
		$ds = (new _hx_array(array()));
		$oldX = 150. + 130 * Math::cos(Math::$PI / 2);
		$oldY = 150. - 130 * Math::sin(Math::$PI / 2);
		$totalAngle = 0;
		{
			$_g = 0;
			while($_g < $values->length) {
				$v = $values[$_g];
				++$_g;
				$angle = 2 * Math::$PI * $v / 100;
				$totalAngle = $totalAngle + $angle;
				$newX = 150. + 130 * Math::cos($totalAngle - Math::$PI / 2);
				$newY = 150. + 130 * Math::sin($totalAngle - Math::$PI / 2);
				$ds->push("M " . _hx_string_rec($oldX, "") . " " . _hx_string_rec($oldY, "") . " A " . _hx_string_rec(130, "") . " " . _hx_string_rec(130, "") . " 0 " . _hx_string_rec(((($angle < Math::$PI) ? 0 : 1)), "") . " 1 " . _hx_string_rec($newX, "") . " " . _hx_string_rec($newY, "") . " L " . _hx_string_rec(150., "") . " " . _hx_string_rec(150., "") . " Z");
				$oldX = $newX;
				$oldY = $newY;
				unset($v,$newY,$newX,$angle);
			}
		}
		return $ds;
	}
	static function calculateMiddlePoints($values, $innerRadiusSize) {
		$ps = (new _hx_array(array()));
		$totalAngle = 0;
		{
			$_g = 0;
			while($_g < $values->length) {
				$v = $values[$_g];
				++$_g;
				$angle = Math::$PI * $v / 100;
				$totalAngle += $angle;
				$labelRadius = 130 * $innerRadiusSize + (130 - 130 * $innerRadiusSize) / 2;
				$newX = 150. + $labelRadius * Math::cos($totalAngle - Math::$PI / 2);
				$newY = 150. + $labelRadius * Math::sin($totalAngle - Math::$PI / 2);
				$p = _hx_anonymous(array("x" => $newX, "y" => $newY));
				$ps->push($p);
				$totalAngle += $angle;
				unset($v,$p,$newY,$newX,$labelRadius,$angle);
			}
		}
		return $ps;
	}
	static function hexToTriad($hex) {
		$cleanHex = _hx_explode("", _hx_substring($hex, _hx_index_of($hex, "#", null) + 1, strlen($hex)));
		$color = _hx_anonymous(array("r" => Std::parseInt("0x" . _hx_string_or_null($cleanHex[0]) . _hx_string_or_null($cleanHex[1])), "g" => Std::parseInt("0x" . _hx_string_or_null($cleanHex[2]) . _hx_string_or_null($cleanHex[3])), "b" => Std::parseInt("0x" . _hx_string_or_null($cleanHex[4]) . _hx_string_or_null($cleanHex[5]))));
		return $color;
	}
	static function calculateOneColor($c1, $c2, $shift) {
		return Std::int($c1 + ($c2 - $c1) * $shift);
	}
	static function calculateColors($baseColors, $valuesLength) {
		$rgbColors = $baseColors->map(array(new _hx_lambda(array(&$baseColors, &$valuesLength), "PieChartGen_0"), 'execute'));
		$newColors = (new _hx_array(array()));
		{
			$_g1 = 0;
			$_g = $valuesLength - 1;
			while($_g1 < $_g) {
				$i = $_g1++;
				$colorPair = $i * ($baseColors->length - 1) / ($valuesLength - 1);
				$colorPairNumber = Math::floor($colorPair);
				$colorPairShift = $colorPair - $colorPairNumber;
				$color = null;
				if($colorPairNumber === $baseColors->length - 1) {
					$color = $rgbColors[$colorPairNumber];
				} else {
					$color = _hx_anonymous(array("r" => PieChartGen::calculateOneColor(_hx_array_get($rgbColors, $colorPairNumber)->r, _hx_array_get($rgbColors, $colorPairNumber + 1)->r, $colorPairShift), "g" => PieChartGen::calculateOneColor(_hx_array_get($rgbColors, $colorPairNumber)->g, _hx_array_get($rgbColors, $colorPairNumber + 1)->g, $colorPairShift), "b" => PieChartGen::calculateOneColor(_hx_array_get($rgbColors, $colorPairNumber)->b, _hx_array_get($rgbColors, $colorPairNumber + 1)->b, $colorPairShift)));
				}
				$newColors->push($color);
				unset($i,$colorPairShift,$colorPairNumber,$colorPair,$color);
			}
		}
		return $newColors;
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
function PieChartGen_0(&$baseColors, &$valuesLength, $c) {
	{
		return PieChartGen::hexToTriad($c);
	}
}
