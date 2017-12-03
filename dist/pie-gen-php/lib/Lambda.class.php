<?php

class Lambda {
	public function __construct(){}
	static function fold($it, $f, $first) {
		if(null == $it) throw new HException('null iterable');
		$__hx__it = $it->iterator();
		while($__hx__it->hasNext()) {
			unset($x);
			$x = $__hx__it->next();
			$first = call_user_func_array($f, array($x, $first));
		}
		return $first;
	}
	function __toString() { return 'Lambda'; }
}
