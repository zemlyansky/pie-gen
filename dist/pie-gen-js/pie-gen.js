// Generated by Haxe 3.4.4
(function ($hx_exports) { "use strict";
var HxOverrides = function() { };
HxOverrides.cca = function(s,index) {
	var x = s.charCodeAt(index);
	if(x != x) {
		return undefined;
	}
	return x;
};
var PieChartGen = function() { };
PieChartGen.normalizeValues = function(values) {
	var sum = 0;
	var _g = 0;
	while(_g < values.length) {
		var v = values[_g];
		++_g;
		sum += v;
	}
	return values.map(function(v1) {
		return v1 * 100 / sum;
	});
};
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
		totalAngle += angle;
		var newX = 150. + 130 * Math.cos(totalAngle - Math.PI / 2);
		var newY = 150. + 130 * Math.sin(totalAngle - Math.PI / 2);
		ds.push("M " + oldX + " " + oldY + " A " + 130 + " " + 130 + " 0 " + (angle < Math.PI ? 0 : 1) + " 1 " + newX + " " + newY + " L " + 150. + " " + 150. + " Z");
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
	var _g = valuesLength;
	while(_g1 < _g) {
		var i = _g1++;
		var colorPair = i * (baseColors.length - 1) / (valuesLength - 1);
		var colorPairNumber = Math.floor(colorPair);
		var colorPairShift = colorPair - colorPairNumber;
		var color;
		if(colorPairNumber == baseColors.length - 1) {
			color = rgbColors[colorPairNumber];
		} else {
			color = { r : PieChartGen.calculateOneColor(rgbColors[colorPairNumber].r,rgbColors[colorPairNumber + 1].r,colorPairShift), g : PieChartGen.calculateOneColor(rgbColors[colorPairNumber].g,rgbColors[colorPairNumber + 1].g,colorPairShift), b : PieChartGen.calculateOneColor(rgbColors[colorPairNumber].b,rgbColors[colorPairNumber + 1].b,colorPairShift)};
		}
		newColors.push(color);
	}
	return newColors;
};
PieChartGen.create = $hx_exports["create"] = function(values,params) {
	var mask = "\n      <mask id=\"donut-mask\">\n        <rect width=\"100%\" height=\"100%\" fill=\"white\"></rect>\n        <circle r=\"" + 130 * params.innerRadiusSize + "\" cx=\"" + 150. + "\" cy=\"" + 150. + "\" fill=\"black\"></circle>\n      </mask>\n    ";
	var groups = "";
	var ds = PieChartGen.calculateArcs(PieChartGen.normalizeValues(values));
	var ps = PieChartGen.calculateMiddlePoints(PieChartGen.normalizeValues(values),params.innerRadiusSize);
	var cs = PieChartGen.calculateColors(params.colors,values.length);
	var _g1 = 0;
	var _g = values.length;
	while(_g1 < _g) {
		var i = _g1++;
		var g = "\n        <g>\n          <path mask=\"url(#donut-mask)\" fill=\"rgb(" + cs[i].r + ", " + cs[i].g + ", " + cs[i].b + ")\" stroke=\"rgb(" + cs[i].r + ", " + cs[i].g + ", " + cs[i].b + ")\" d=\"" + ds[i] + "\"></path>\n          <text fill=\"white\" stroke=\"none\" text-anchor=\"middle\" font-size=\"10px\" font-family=\"sans-serif\" x=\"" + ps[i].x + "\" y=\"" + (ps[i].y + 5) + "\">" + values[i] + "</text>\n        </g>\n      ";
		groups += g;
	}
	var output = "\n      <svg viewBox=\"0 0 " + 300 + " " + 300 + "\" preserveAspectRatio=\"xMinYMin meet\">\n        " + mask + "\n        " + groups + "\n      </svg>\n    ";
	return output;
};
var Std = function() { };
Std.parseInt = function(x) {
	var v = parseInt(x,10);
	if(v == 0 && (HxOverrides.cca(x,1) == 120 || HxOverrides.cca(x,1) == 88)) {
		v = parseInt(x);
	}
	if(isNaN(v)) {
		return null;
	}
	return v;
};
PieChartGen.SIZE = 300;
PieChartGen.RADIUS = 130;
})(typeof exports != "undefined" ? exports : typeof window != "undefined" ? window : typeof self != "undefined" ? self : this);
