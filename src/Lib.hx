// using Lambda;

#if php
  import php.Lib;
#end

typedef Point = {x: Float, y: Float}
typedef Color = {r: Int, g: Int, b: Int}

class PieChartGen {
  inline static var SIZE = 300;
  inline static var RADIUS = 130;

  /**
   * Scale values to have 100% sum
   * @param {Number[]} values
   * @returns {Number[]}
   */
  private static function normalizeValues
  (
    values: Array<Float>
  )
  : Array<Float>
  {
    var sum: Float = 0;
    for (v in values) {
      sum += v;
    }
    return values.map(function (v) return v * 100 / sum);
  }
  /**
   * Calculate 'd' attributes for 'path' svg elements
   * @param {Number[]} values - array of values
   * @returns {String[]} - array of 'd' values
   */
  private static function calculateArcs
  (
    values: Array<Float>
  )
  : Array<String>
  {
    var a = 100;
    var ds = [];
    var oldX = SIZE / 2 + RADIUS * (Math.cos(Math.PI / 2));
    var oldY = SIZE / 2 - RADIUS * (Math.sin(Math.PI / 2));
    var totalAngle: Float = 0;
    for (v in values) {
      var angle = 2 * Math.PI * v / 100;
      totalAngle = totalAngle + angle;
      var newX = SIZE / 2 + RADIUS * (Math.cos(totalAngle - Math.PI / 2));
      var newY = SIZE / 2 + RADIUS * (Math.sin(totalAngle - Math.PI / 2));
      ds.push('M ${oldX} ${oldY} A ${RADIUS} ${RADIUS} 0 ${(angle < Math.PI) ? 0 : 1} 1 ${newX} ${newY} L ${SIZE / 2} ${SIZE / 2} Z');
      oldX = newX;
      oldY = newY;
    }
    return ds;
  }

  /**
   * Calculate centers of arcs to place labels
   * @param {Number[]} values - array of values
   * @returns {Object[]} - array of pairs {x, y}
   */
  private static function calculateMiddlePoints
  (
    values: Array<Float>,
    innerRadiusSize: Float
  )
  : Array<Point>
  {
    var ps = [];
    var totalAngle: Float = 0;
    for (v in values) {
      var angle = Math.PI * v / 100;
      totalAngle += angle;
      var labelRadius = (RADIUS * innerRadiusSize + (RADIUS - RADIUS * innerRadiusSize) / 2);
      var newX = SIZE / 2 + labelRadius * (Math.cos(totalAngle - Math.PI / 2));
      var newY = SIZE / 2 + labelRadius * (Math.sin(totalAngle - Math.PI / 2));
      var p: Point = {x: newX, y: newY};
      ps.push(p);
      totalAngle += angle;
    }
    return ps;
  }

  /**
   * Calculate r,g,b, values from hex string
   * @param {String} hex - string with a hex value
   * @returns {Object} - object with decimal {r,g,b} values
   */
  private static function hexToTriad 
  (
    hex: String
  )
  : Color
  {
    var cleanHex = hex
        .substring(hex.indexOf('#') + 1, hex.length)
        .split('');
    var color: Color = {
      r: Std.parseInt('0x' + cleanHex[0] + cleanHex[1]),
      g: Std.parseInt('0x' + cleanHex[2] + cleanHex[3]),
      b: Std.parseInt('0x' + cleanHex[4] + cleanHex[5])
    };
    return color;
  }

  /**
   * Calculates one color shift
   */
  private static function calculateOneColor 
  (
    c1: Int,
    c2: Int,
    shift: Float
  )
  : Int
  {
    return Std.int(c1 + (c2 - c1) * shift);
  }

  /**
   * Interpolates base color to match values length
   */
  private static function calculateColors
  (
    baseColors: Array<Dynamic>,
    valuesLength: Int
  )
  : Array<Color>
  {
    var rgbColors = baseColors.map(function (c) return hexToTriad(c));
    var newColors = [];

    for (i in 0...valuesLength) {
      var colorPair = (i * (baseColors.length - 1) / (valuesLength - 1));
      var colorPairNumber = Math.floor(colorPair);
      var colorPairShift = colorPair - colorPairNumber;
      var color: Color;
      if (colorPairNumber == (baseColors.length - 1)) {
        color = rgbColors[colorPairNumber];
      } else {
        color = {
          r: calculateOneColor(rgbColors[colorPairNumber].r, rgbColors[colorPairNumber + 1].r, colorPairShift),
          g: calculateOneColor(rgbColors[colorPairNumber].g, rgbColors[colorPairNumber + 1].g, colorPairShift),
          b: calculateOneColor(rgbColors[colorPairNumber].b, rgbColors[colorPairNumber + 1].b, colorPairShift)
        };
      }
      newColors.push(color);
    }

    return newColors;
  }

  /**
   * Exported function
   */
  @:expose('create')
  public static function create
  (
    values: Dynamic,
    params: Dynamic
  )
  : String
  {
    // var colors: Array<Dynamic> = [];
    // Convert native PHP arrays to HAXE types
    #if php
      values = php.Lib.toHaxeArray(values);
      var paramsMap = php.Lib.hashOfAssociativeArray(params);
      var newParams: Dynamic = {};
      for (key in paramsMap.keys()) {
        var value: Dynamic = paramsMap.get(key);
        if (key == 'colors') {
          value = php.Lib.toHaxeArray(value); 
        }
        Reflect.setField(newParams, key, value);
      }
      params = newParams;
      //params.colors = php.Lib.toHaxeArray(params.colors);
      //trace('params:');
      //params = {
      //  innerRadiusSize: tempparams['innerRadiusSize'],
      //  colors: php.Lib.toHaxeArray(tempparams['colors'])
      //}
      // params = php.Lib.hashOfAssociativeArray(params);
      // trace(params.colors);
      //  .map(function (c) return '' + c);
    #end
    // Convert native Python dict to HAXE object
    #if python
      params = python.Lib.dictToAnon(params);
    #end

    var mask: String = '
      <mask id="donut-mask">
        <rect width="100%" height="100%" fill="white"></rect>
        <circle r="${RADIUS * params.innerRadiusSize}" cx="${SIZE / 2}" cy="${SIZE / 2}" fill="black"></circle>
      </mask>
    ';

    var groups: String = '';
    var ds: Array<String> = calculateArcs(normalizeValues(values));
    var ps: Array<Point> = calculateMiddlePoints(normalizeValues(values), params.innerRadiusSize);
    var cs: Array<Color> = calculateColors(params.colors, values.length);
    for (i in 0...values.length) {
      var g: String = '
        <g>
          <path mask="url(#donut-mask)" fill="rgb(${cs[i].r}, ${cs[i].g}, ${cs[i].b})" stroke="rgb(${cs[i].r}, ${cs[i].g}, ${cs[i].b})" d="${ds[i]}"></path>
          <text fill="white" stroke="none" text-anchor="middle" font-size="10px" font-family="sans-serif" x="${ps[i].x}" y="${ps[i].y + 5}">${values[i]}</text>
        </g>
      ';
      groups += g;
    }
    // Final output string that contain SVG code
    //  <svg viewBox="0 0 ${SIZE} ${SIZE}" preserveAspectRatio="xMinYMin meet" style="display: inline-block; position: absolute; top: 0px; left: 0px;">
    var output: String = '
      <svg viewBox="0 0 ${SIZE} ${SIZE}" preserveAspectRatio="xMinYMin meet">
        ${mask}
        ${groups}
      </svg>
    ';
    return output;
  }
}
