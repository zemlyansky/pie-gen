<?php

class PieChartGen {
	public function __construct(){}
	static $SIZE = 300;
	static $RADIUS = 130;
	static function normalizeValues($values) {
		$sum = 0;
		{
			$_g = 0;
			while($_g < $values->length) {
				$v = $values[$_g];
				++$_g;
				$sum += $v;
				unset($v);
			}
		}
		return $values->map(array(new _hx_lambda(array(&$sum, &$values), "PieChartGen_0"), 'execute'));
	}
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
		$rgbColors = $baseColors->map(array(new _hx_lambda(array(&$baseColors, &$valuesLength), "PieChartGen_1"), 'execute'));
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
	static function create($values, $params) {
		$colors = (new _hx_array(array()));
		{
			$a = $values;
			$values = new _hx_array($a);
		}
		$newparams = php_Lib::hashOfAssociativeArray($params);
		haxe_Log::trace($newparams->toString(), _hx_anonymous(array("fileName" => "Lib.hx", "lineNumber" => 170, "className" => "PieChartGen", "methodName" => "create")));
		$mask = "\x0A      <mask id=\"donut-mask\">\x0A        <rect width=\"100%\" height=\"100%\" fill=\"white\"></rect>\x0A        <circle r=" . _hx_string_rec(130 * $params->innerRadiusSize, "") . " cx=" . _hx_string_rec(150., "") . " cy=" . _hx_string_rec(150., "") . " fill=\"black\"></circle>\x0A      </mask>\x0A    ";
		$groups = "";
		{
			$_g1 = 0;
			$_g = _hx_len($values);
			while($_g1 < $_g) {
				$i = $_g1++;
				$g = "\x0A        <g>\x0A          <path mask=\"url(#donut-mask)\"></path>\x0A          <text fill=\"white\" stroke=\"none\" text-anchor=\"middle\" font-size=\"10px\" font-family=\"sans-serif\"></text>\x0A        </g>\x0A      ";
				$groups .= _hx_string_or_null($g);
				unset($i,$g);
			}
		}
		$output = "\x0A      <svg viewBox=\"0 0 " . _hx_string_rec(300, "") . " " . _hx_string_rec(300, "") . "\" preserveAspectRatio=\"xMinYMin meet\" style=\"display: inline-block; position: absolute; top: 0px; left: 0px;\">\x0A        " . _hx_string_or_null($mask) . "\x0A        " . _hx_string_or_null($groups) . "\x0A      </svg>\x0A    ";
		return $output;
	}
	function __toString() { return 'PieChartGen'; }
}
function PieChartGen_0(&$sum, &$values, $v1) {
	{
		return $v1 * 100 / $sum;
	}
}
function PieChartGen_1(&$baseColors, &$valuesLength, $c) {
	{
		return PieChartGen::hexToTriad($c);
	}
}
