#if php
import php.Lib;
#end

class PieChartGen {
  inline static var SIZE = 302;
  inline static var RADIUS = 150;

  @:expose('generate')
  public static function calculateArcs (values:Array<Float>):Array<String> {
    var a = 100;
    var ds = [];
    var oldX = SIZE / 2 + RADIUS * (Math.cos(Math.PI / 2));
    var oldY = SIZE / 2 - RADIUS * (Math.sin(Math.PI / 2));
    var totalAngle:Float = 0;
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

  public static function run(arr: Dynamic) {
    #if php
      arr = php.Lib.toHaxeArray(arr);
    #end
    return arr.length;
  }
}
