import sys
sys.path.append("../dist/pie-gen-py")
from PieGen import PieChartGen 
print(PieChartGen.create([1,24,40], {
  'innerRadiusSize': 0.1,
  'colors': ['#344122','#415214']
}))
