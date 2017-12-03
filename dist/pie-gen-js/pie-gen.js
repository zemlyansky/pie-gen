(function (console, $hx_exports) { "use strict";
var PieChartGen = function() { };
PieChartGen.calculateArcs = $hx_exports.generate = function(values) {
	var a = 100;
	var ds = [];
	var oldX = 151. + 150 * Math.cos(Math.PI / 2);
	var oldY = 151. - 150 * Math.sin(Math.PI / 2);
	var totalAngle = 0;
	var _g = 0;
	while(_g < values.length) {
		var v = values[_g];
		++_g;
		var angle = 2 * Math.PI * v / 100;
		totalAngle = totalAngle + angle;
		var newX = 151. + 150 * Math.cos(totalAngle - Math.PI / 2);
		var newY = 151. + 150 * Math.sin(totalAngle - Math.PI / 2);
		ds.push("M " + oldX + " " + oldY + " A " + 150 + " " + 150 + " 0 " + (angle < Math.PI?0:1) + " 1 " + newX + " " + newY + " L " + 151. + " " + 151. + " Z");
		oldX = newX;
		oldY = newY;
	}
	return ds;
};
PieChartGen.run = function(arr) {
	return arr.length;
};
PieChartGen.SIZE = 302;
PieChartGen.RADIUS = 150;
})(typeof console != "undefined" ? console : {log:function(){}}, typeof window != "undefined" ? window : exports);
