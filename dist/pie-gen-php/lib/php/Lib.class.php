<?php

class php_Lib {
	public function __construct(){}
	static function hashOfAssociativeArray($arr) {
		$h = new haxe_ds_StringMap();
		$h->h = $arr;
		return $h;
	}
	function __toString() { return 'php.Lib'; }
}
