<?php

// Generated by Haxe 3.4.4
class Math {
	public function __construct(){}
	static $PI;
	static $NaN;
	static $POSITIVE_INFINITY;
	static $NEGATIVE_INFINITY;
	static function sin($v) {
		return sin($v);
	}
	static function cos($v) {
		return cos($v);
	}
	static function floor($v) {
		return (int) floor($v);
	}
	function __toString() { return 'Math'; }
}
{
	Math::$PI = M_PI;
	Math::$NaN = acos(1.01);
	Math::$NEGATIVE_INFINITY = log(0);
	Math::$POSITIVE_INFINITY = -Math::$NEGATIVE_INFINITY;
}
