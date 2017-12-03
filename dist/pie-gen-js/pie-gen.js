(function (console, $hx_exports) { "use strict";
var HxOverrides = function() { };
HxOverrides.cca = function(s,index) {
	var x = s.charCodeAt(index);
	if(x != x) return undefined;
	return x;
};
var PieChartGen = $hx_exports.generate = function() { };
PieChartGen.calculateArcs = function(values) {
	var a = 100;
	var ds = [];
	var oldX = 150. + 130 * Math.cos(Math.PI / 2);
	var oldY = 150. - 130 * Math.sin(Math.PI / 2);
	var totalAngle = 0;
	var _g = 0;
	while(_g < values.length) {
		var v = values[_g];
		++_g;
		var angle = 2 * Math.PI * v / 100;
		totalAngle = totalAngle + angle;
		var newX = 150. + 130 * Math.cos(totalAngle - Math.PI / 2);
		var newY = 150. + 130 * Math.sin(totalAngle - Math.PI / 2);
		ds.push("M " + oldX + " " + oldY + " A " + 130 + " " + 130 + " 0 " + (angle < Math.PI?0:1) + " 1 " + newX + " " + newY + " L " + 150. + " " + 150. + " Z");
		oldX = newX;
		oldY = newY;
	}
	return ds;
};
PieChartGen.calculateMiddlePoints = function(values,innerRadiusSize) {
	var ps = [];
	var totalAngle = 0;
	var _g = 0;
	while(_g < values.length) {
		var v = values[_g];
		++_g;
		var angle = Math.PI * v / 100;
		totalAngle += angle;
		var labelRadius = 130 * innerRadiusSize + (130 - 130 * innerRadiusSize) / 2;
		var newX = 150. + labelRadius * Math.cos(totalAngle - Math.PI / 2);
		var newY = 150. + labelRadius * Math.sin(totalAngle - Math.PI / 2);
		var p = { x : newX, y : newY};
		ps.push(p);
		totalAngle += angle;
	}
	return ps;
};
PieChartGen.hexToTriad = function(hex) {
	var cleanHex = hex.substring(hex.indexOf("#") + 1,hex.length).split("");
	var color = { r : Std.parseInt("0x" + cleanHex[0] + cleanHex[1]), g : Std.parseInt("0x" + cleanHex[2] + cleanHex[3]), b : Std.parseInt("0x" + cleanHex[4] + cleanHex[5])};
	return color;
};
PieChartGen.calculateOneColor = function(c1,c2,shift) {
	return c1 + (c2 - c1) * shift | 0;
};
PieChartGen.calculateColors = function(baseColors,valuesLength) {
	var rgbColors = baseColors.map(function(c) {
		return PieChartGen.hexToTriad(c);
	});
	var newColors = [];
	var _g1 = 0;
	var _g = valuesLength - 1;
	while(_g1 < _g) {
		var i = _g1++;
		var colorPair = i * (baseColors.length - 1) / (valuesLength - 1);
		var colorPairNumber = Math.floor(colorPair);
		var colorPairShift = colorPair - colorPairNumber;
		var color;
		if(colorPairNumber == baseColors.length - 1) color = rgbColors[colorPairNumber]; else color = { r : PieChartGen.calculateOneColor(rgbColors[colorPairNumber].r,rgbColors[colorPairNumber + 1].r,colorPairShift), g : PieChartGen.calculateOneColor(rgbColors[colorPairNumber].g,rgbColors[colorPairNumber + 1].g,colorPairShift), b : PieChartGen.calculateOneColor(rgbColors[colorPairNumber].b,rgbColors[colorPairNumber + 1].b,colorPairShift)};
		newColors.push(color);
	}
	return newColors;
};
PieChartGen.run = function(arr) {
	return arr.length;
};
var Std = function() { };
Std.parseInt = function(x) {
	var v = parseInt(x,10);
	if(v == 0 && (HxOverrides.cca(x,1) == 120 || HxOverrides.cca(x,1) == 88)) v = parseInt(x);
	if(isNaN(v)) return null;
	return v;
};
if(Array.prototype.map == null) Array.prototype.map = function(f) {
	var a = [];
	var _g1 = 0;
	var _g = this.length;
	while(_g1 < _g) {
		var i = _g1++;
		a[i] = f(this[i]);
	}
	return a;
};
PieChartGen.SIZE = 300;
PieChartGen.RADIUS = 130;
})(typeof console != "undefined" ? console : {log:function(){}}, typeof window != "undefined" ? window : exports);
