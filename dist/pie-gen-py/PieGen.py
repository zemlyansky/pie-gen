import math as python_lib_Math
import math as Math
import functools as python_lib_Functools
import inspect as python_lib_Inspect


class _hx_AnonObject:
	def __init__(self, fields):
		self.__dict__ = fields


class Enum:
	_hx_class_name = "Enum"
	_hx_fields = ["tag", "index", "params"]
	_hx_methods = ["__str__"]

	def __init__(self,tag,index,params):
		self.tag = None
		self.index = None
		self.params = None
		self.tag = tag
		self.index = index
		self.params = params

	def __str__(self):
		if (self.params is None):
			return self.tag
		else:
			return (((HxOverrides.stringOrNull(self.tag) + "(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in self.params]))) + ")")



class PieChartGen:
	_hx_class_name = "PieChartGen"
	_hx_statics = ["SIZE", "RADIUS", "normalizeValues", "calculateArcs", "calculateMiddlePoints", "hexToTriad", "calculateOneColor", "calculateColors", "create"]

	@staticmethod
	def normalizeValues(values):
		sum = 0
		_g = 0
		while (_g < len(values)):
			v = (values[_g] if _g >= 0 and _g < len(values) else None)
			_g = (_g + 1)
			sum = (sum + v)
		def _hx_local_3():
			def _hx_local_2(v1):
				return ((v1 * 100) / sum)
			return list(map(_hx_local_2,values))
		return _hx_local_3()

	@staticmethod
	def calculateArcs(values):
		a = 100
		ds = []
		oldX = None
		def _hx_local_0():
			v = (Math.PI / 2)
			return (Math.NaN if (((v == Math.POSITIVE_INFINITY) or ((v == Math.NEGATIVE_INFINITY)))) else python_lib_Math.cos(v))
		oldX = (150. + ((130 * _hx_local_0())))
		oldY = None
		def _hx_local_1():
			v1 = (Math.PI / 2)
			return (Math.NaN if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else python_lib_Math.sin(v1))
		oldY = (150. - ((130 * _hx_local_1())))
		totalAngle = 0
		_g = 0
		while (_g < len(values)):
			v2 = (values[_g] if _g >= 0 and _g < len(values) else None)
			_g = (_g + 1)
			angle = (((2 * Math.PI) * v2) / 100)
			totalAngle = (totalAngle + angle)
			newX = None
			def _hx_local_3():
				v3 = (totalAngle - ((Math.PI / 2)))
				return (Math.NaN if (((v3 == Math.POSITIVE_INFINITY) or ((v3 == Math.NEGATIVE_INFINITY)))) else python_lib_Math.cos(v3))
			newX = (150. + ((130 * _hx_local_3())))
			newY = None
			def _hx_local_4():
				v4 = (totalAngle - ((Math.PI / 2)))
				return (Math.NaN if (((v4 == Math.POSITIVE_INFINITY) or ((v4 == Math.NEGATIVE_INFINITY)))) else python_lib_Math.sin(v4))
			newY = (150. + ((130 * _hx_local_4())))
			ds.append((((((((((((((((((("M " + str(oldX)) + " ") + str(oldY)) + " A ") + str(130)) + " ") + str(130)) + " 0 ") + str(((0 if ((angle < Math.PI)) else 1)))) + " 1 ") + str(newX)) + " ") + str(newY)) + " L ") + str(150.)) + " ") + str(150.)) + " Z"))
			oldX = newX
			oldY = newY
		return ds

	@staticmethod
	def calculateMiddlePoints(values,innerRadiusSize):
		ps = []
		totalAngle = 0
		_g = 0
		while (_g < len(values)):
			v = (values[_g] if _g >= 0 and _g < len(values) else None)
			_g = (_g + 1)
			angle = ((Math.PI * v) / 100)
			totalAngle = (totalAngle + angle)
			labelRadius = ((130 * innerRadiusSize) + ((((130 - ((130 * innerRadiusSize)))) / 2)))
			newX = None
			def _hx_local_2():
				v1 = (totalAngle - ((Math.PI / 2)))
				return (Math.NaN if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else python_lib_Math.cos(v1))
			newX = (150. + ((labelRadius * _hx_local_2())))
			newY = None
			def _hx_local_3():
				v2 = (totalAngle - ((Math.PI / 2)))
				return (Math.NaN if (((v2 == Math.POSITIVE_INFINITY) or ((v2 == Math.NEGATIVE_INFINITY)))) else python_lib_Math.sin(v2))
			newY = (150. + ((labelRadius * _hx_local_3())))
			p = _hx_AnonObject({'x': newX, 'y': newY})
			ps.append(p)
			totalAngle = (totalAngle + angle)
		return ps

	@staticmethod
	def hexToTriad(hex):
		cleanHex = None
		_this = None
		startIndex = (hex.find("#") + 1)
		_this = HxString.substring(hex,startIndex,len(hex))
		cleanHex = list(_this)
		color = _hx_AnonObject({'r': Std.parseInt((("0x" + HxOverrides.stringOrNull((cleanHex[0] if 0 < len(cleanHex) else None))) + HxOverrides.stringOrNull((cleanHex[1] if 1 < len(cleanHex) else None)))), 'g': Std.parseInt((("0x" + HxOverrides.stringOrNull((cleanHex[2] if 2 < len(cleanHex) else None))) + HxOverrides.stringOrNull((cleanHex[3] if 3 < len(cleanHex) else None)))), 'b': Std.parseInt((("0x" + HxOverrides.stringOrNull((cleanHex[4] if 4 < len(cleanHex) else None))) + HxOverrides.stringOrNull((cleanHex[5] if 5 < len(cleanHex) else None))))})
		return color

	@staticmethod
	def calculateOneColor(c1,c2,shift):
		def _hx_local_2():
			def _hx_local_1():
				_hx_local_0 = None
				try:
					_hx_local_0 = int((c1 + ((((c2 - c1)) * shift))))
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e = _hx_e1
					_hx_local_0 = None
				return _hx_local_0
			return _hx_local_1()
		return _hx_local_2()

	@staticmethod
	def calculateColors(baseColors,valuesLength):
		def _hx_local_0(c):
			return PieChartGen.hexToTriad(c)
		rgbColors = list(map(_hx_local_0,baseColors))
		newColors = []
		_g1 = 0
		_g = (valuesLength - 1)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			colorPair = ((i * ((len(baseColors) - 1))) / ((valuesLength - 1)))
			colorPairNumber = Math.floor(colorPair)
			colorPairShift = (colorPair - colorPairNumber)
			color = None
			if (colorPairNumber == ((len(baseColors) - 1))):
				color = (rgbColors[colorPairNumber] if colorPairNumber >= 0 and colorPairNumber < len(rgbColors) else None)
			else:
				color = _hx_AnonObject({'r': PieChartGen.calculateOneColor((rgbColors[colorPairNumber] if colorPairNumber >= 0 and colorPairNumber < len(rgbColors) else None).r,python_internal_ArrayImpl._get(rgbColors, (colorPairNumber + 1)).r,colorPairShift), 'g': PieChartGen.calculateOneColor((rgbColors[colorPairNumber] if colorPairNumber >= 0 and colorPairNumber < len(rgbColors) else None).g,python_internal_ArrayImpl._get(rgbColors, (colorPairNumber + 1)).g,colorPairShift), 'b': PieChartGen.calculateOneColor((rgbColors[colorPairNumber] if colorPairNumber >= 0 and colorPairNumber < len(rgbColors) else None).b,python_internal_ArrayImpl._get(rgbColors, (colorPairNumber + 1)).b,colorPairShift)})
			newColors.append(color)
		return newColors

	@staticmethod
	def create(values,params):
		colors = []
		params = python_Lib.dictToAnon(params)
		mask = (((((("\n      <mask id=\"donut-mask\">\n        <rect width=\"100%\" height=\"100%\" fill=\"white\"></rect>\n        <circle r=" + str((130 * Reflect.field(params,"innerRadiusSize")))) + " cx=") + str(150.)) + " cy=") + str(150.)) + " fill=\"black\"></circle>\n      </mask>\n    ")
		groups = ""
		_g1 = 0
		_g = Reflect.field(values,"length")
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			g = "\n        <g>\n          <path mask=\"url(#donut-mask)\"></path>\n          <text fill=\"white\" stroke=\"none\" text-anchor=\"middle\" font-size=\"10px\" font-family=\"sans-serif\"></text>\n        </g>\n      "
			groups = (("null" if groups is None else groups) + ("null" if g is None else g))
		output = (((((((("\n      <svg viewBox=\"0 0 " + str(300)) + " ") + str(300)) + "\" preserveAspectRatio=\"xMinYMin meet\" style=\"display: inline-block; position: absolute; top: 0px; left: 0px;\">\n        ") + ("null" if mask is None else mask)) + "\n        ") + ("null" if groups is None else groups)) + "\n      </svg>\n    ")
		return output


class Reflect:
	_hx_class_name = "Reflect"
	_hx_statics = ["field"]

	@staticmethod
	def field(o,field):
		return python_Boot.field(o,field)


class Std:
	_hx_class_name = "Std"
	_hx_statics = ["parseInt", "shortenPossibleNumber", "parseFloat"]

	@staticmethod
	def parseInt(x):
		if (x is None):
			return None
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			try:
				prefix = None
				_this = HxString.substr(x,0,2)
				prefix = _this.lower()
				if (prefix == "0x"):
					return int(x,16)
				raise _HxException("fail")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				r = None
				x1 = Std.parseFloat(x)
				try:
					r = int(x1)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					r = None
				if (r is None):
					r1 = Std.shortenPossibleNumber(x)
					if (r1 != x):
						return Std.parseInt(r1)
					else:
						return None
				return r

	@staticmethod
	def shortenPossibleNumber(x):
		r = ""
		_g1 = 0
		_g = len(x)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			c = None
			if ((i < 0) or ((i >= len(x)))):
				c = ""
			else:
				c = x[i]
			_g2 = HxString.charCodeAt(c,0)
			if (_g2 is not None):
				if (((((((((((_g2 == 46) or ((_g2 == 57))) or ((_g2 == 56))) or ((_g2 == 55))) or ((_g2 == 54))) or ((_g2 == 53))) or ((_g2 == 52))) or ((_g2 == 51))) or ((_g2 == 50))) or ((_g2 == 49))) or ((_g2 == 48))):
					r = (("null" if r is None else r) + ("null" if c is None else c))
				else:
					break
			else:
				break
		return r

	@staticmethod
	def parseFloat(x):
		try:
			return float(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			if (x is not None):
				r1 = Std.shortenPossibleNumber(x)
				if (r1 != x):
					return Std.parseFloat(r1)
			return Math.NaN


class python_Boot:
	_hx_class_name = "python.Boot"
	_hx_statics = ["keywords", "toString1", "fields", "simpleField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

	@staticmethod
	def toString1(o,s):
		if (o is None):
			return "null"
		if isinstance(o,str):
			return o
		if (s is None):
			s = ""
		if (len(s) >= 5):
			return "<...>"
		if isinstance(o,bool):
			if o:
				return "true"
			else:
				return "false"
		if isinstance(o,int):
			return str(o)
		if isinstance(o,float):
			try:
				if (o == int(o)):
					def _hx_local_1():
						def _hx_local_0():
							v = o
							return Math.floor((v + 0.5))
						return str(_hx_local_0())
					return _hx_local_1()
				else:
					return str(o)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				return str(o)
		if isinstance(o,list):
			o1 = o
			l = len(o1)
			st = "["
			s = (("null" if s is None else s) + "\t")
			_g = 0
			while (_g < l):
				i = _g
				_g = (_g + 1)
				prefix = ""
				if (i > 0):
					prefix = ","
				st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
			st = (("null" if st is None else st) + "]")
			return st
		try:
			if hasattr(o,"toString"):
				return o.toString()
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		if (python_lib_Inspect.isfunction(o) or python_lib_Inspect.ismethod(o)):
			return "<function>"
		if hasattr(o,"__class__"):
			if isinstance(o,_hx_AnonObject):
				toStr = None
				try:
					fields = python_Boot.fields(o)
					fieldsStr = None
					_g1 = []
					_g11 = 0
					while (_g11 < len(fields)):
						f = (fields[_g11] if _g11 >= 0 and _g11 < len(fields) else None)
						_g11 = (_g11 + 1)
						x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
						_g1.append(x)
					fieldsStr = _g1
					toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					return "{ ... }"
				if (toStr is None):
					return "{ ... }"
				else:
					return toStr
			if isinstance(o,Enum):
				o2 = o
				l1 = len(o2.params)
				hasParams = (l1 > 0)
				if hasParams:
					paramsStr = ""
					_g2 = 0
					while (_g2 < l1):
						i1 = _g2
						_g2 = (_g2 + 1)
						prefix1 = ""
						if (i1 > 0):
							prefix1 = ","
						paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix1 is None else prefix1) + HxOverrides.stringOrNull(python_Boot.toString1((o2.params[i1] if i1 >= 0 and i1 < len(o2.params) else None),s))))))
					return (((HxOverrides.stringOrNull(o2.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
				else:
					return o2.tag
			if hasattr(o,"_hx_class_name"):
				if (o.__class__.__name__ != "type"):
					fields1 = python_Boot.getInstanceFields(o)
					fieldsStr1 = None
					_g3 = []
					_g12 = 0
					while (_g12 < len(fields1)):
						f1 = (fields1[_g12] if _g12 >= 0 and _g12 < len(fields1) else None)
						_g12 = (_g12 + 1)
						x1 = ((("" + ("null" if f1 is None else f1)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f1),(("null" if s is None else s) + "\t"))))
						_g3.append(x1)
					fieldsStr1 = _g3
					toStr1 = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr1]))) + " )")
					return toStr1
				else:
					fields2 = python_Boot.getClassFields(o)
					fieldsStr2 = None
					_g4 = []
					_g13 = 0
					while (_g13 < len(fields2)):
						f2 = (fields2[_g13] if _g13 >= 0 and _g13 < len(fields2) else None)
						_g13 = (_g13 + 1)
						x2 = ((("" + ("null" if f2 is None else f2)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f2),(("null" if s is None else s) + "\t"))))
						_g4.append(x2)
					fieldsStr2 = _g4
					toStr2 = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr2]))) + " )")
					return toStr2
			if (o == str):
				return "#String"
			if (o == list):
				return "#Array"
			if callable(o):
				return "function"
			try:
				if hasattr(o,"__repr__"):
					return o.__repr__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
			if hasattr(o,"__str__"):
				return o.__str__([])
			if hasattr(o,"__name__"):
				return o.__name__
			return "???"
		else:
			return str(o)

	@staticmethod
	def fields(o):
		a = []
		if (o is not None):
			if hasattr(o,"_hx_fields"):
				fields = o._hx_fields
				return list(fields)
			if isinstance(o,_hx_AnonObject):
				d = o.__dict__
				keys = d.keys()
				handler = python_Boot.unhandleKeywords
				for k in keys:
					a.append(handler(k))
			elif hasattr(o,"__dict__"):
				a1 = []
				d1 = o.__dict__
				keys1 = d1.keys()
				for k in keys1:
					a.append(k)
		return a

	@staticmethod
	def simpleField(o,field):
		if (field is None):
			return None
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def field(o,field):
		if (field is None):
			return None
		_hx_local_0 = len(field)
		if (_hx_local_0 == 10):
			if (field == "charCodeAt"):
				if isinstance(o,str):
					s4 = o
					def _hx_local_1(a11):
						return HxString.charCodeAt(s4,a11)
					return _hx_local_1
		elif (_hx_local_0 == 11):
			if (field == "toLowerCase"):
				if isinstance(o,str):
					s1 = o
					def _hx_local_2():
						return HxString.toLowerCase(s1)
					return _hx_local_2
			elif (field == "toUpperCase"):
				if isinstance(o,str):
					s2 = o
					def _hx_local_3():
						return HxString.toUpperCase(s2)
					return _hx_local_3
			elif (field == "lastIndexOf"):
				if isinstance(o,str):
					s6 = o
					def _hx_local_4(a13):
						return HxString.lastIndexOf(s6,a13)
					return _hx_local_4
				elif isinstance(o,list):
					a2 = o
					def _hx_local_5(x2):
						return python_internal_ArrayImpl.lastIndexOf(a2,x2)
					return _hx_local_5
		elif (_hx_local_0 == 9):
			if (field == "substring"):
				if isinstance(o,str):
					s9 = o
					def _hx_local_6(a15):
						return HxString.substring(s9,a15)
					return _hx_local_6
		elif (_hx_local_0 == 5):
			if (field == "split"):
				if isinstance(o,str):
					s7 = o
					def _hx_local_7(d):
						return HxString.split(s7,d)
					return _hx_local_7
			elif (field == "shift"):
				if isinstance(o,list):
					x14 = o
					def _hx_local_8():
						return python_internal_ArrayImpl.shift(x14)
					return _hx_local_8
			elif (field == "slice"):
				if isinstance(o,list):
					x15 = o
					def _hx_local_9(a18):
						return python_internal_ArrayImpl.slice(x15,a18)
					return _hx_local_9
		elif (_hx_local_0 == 4):
			if (field == "copy"):
				if isinstance(o,list):
					def _hx_local_10():
						x6 = o
						return list(x6)
					return _hx_local_10
			elif (field == "join"):
				if isinstance(o,list):
					def _hx_local_11(sep):
						x9 = o
						return sep.join([python_Boot.toString1(x1,'') for x1 in x9])
					return _hx_local_11
			elif (field == "push"):
				if isinstance(o,list):
					x11 = o
					def _hx_local_12(e):
						return python_internal_ArrayImpl.push(x11,e)
					return _hx_local_12
			elif (field == "sort"):
				if isinstance(o,list):
					x16 = o
					def _hx_local_13(f2):
						python_internal_ArrayImpl.sort(x16,f2)
					return _hx_local_13
		elif (_hx_local_0 == 7):
			if (field == "indexOf"):
				if isinstance(o,str):
					s5 = o
					def _hx_local_14(a12):
						return HxString.indexOf(s5,a12)
					return _hx_local_14
				elif isinstance(o,list):
					a = o
					def _hx_local_15(x1):
						return python_internal_ArrayImpl.indexOf(a,x1)
					return _hx_local_15
			elif (field == "unshift"):
				if isinstance(o,list):
					x12 = o
					def _hx_local_16(e1):
						python_internal_ArrayImpl.unshift(x12,e1)
					return _hx_local_16
			elif (field == "reverse"):
				if isinstance(o,list):
					a4 = o
					def _hx_local_17():
						python_internal_ArrayImpl.reverse(a4)
					return _hx_local_17
		elif (_hx_local_0 == 3):
			if (field == "map"):
				if isinstance(o,list):
					x4 = o
					def _hx_local_18(f):
						return python_internal_ArrayImpl.map(x4,f)
					return _hx_local_18
			elif (field == "pop"):
				if isinstance(o,list):
					x10 = o
					def _hx_local_19():
						return python_internal_ArrayImpl.pop(x10)
					return _hx_local_19
		elif (_hx_local_0 == 8):
			if (field == "toString"):
				if isinstance(o,str):
					s10 = o
					def _hx_local_20():
						return HxString.toString(s10)
					return _hx_local_20
				elif isinstance(o,list):
					x3 = o
					def _hx_local_21():
						return python_internal_ArrayImpl.toString(x3)
					return _hx_local_21
			elif (field == "iterator"):
				if isinstance(o,list):
					x7 = o
					def _hx_local_22():
						return python_internal_ArrayImpl.iterator(x7)
					return _hx_local_22
		elif (_hx_local_0 == 6):
			if (field == "length"):
				if isinstance(o,str):
					s = o
					return len(s)
				elif isinstance(o,list):
					x = o
					return len(x)
			elif (field == "charAt"):
				if isinstance(o,str):
					s3 = o
					def _hx_local_23(a1):
						return HxString.charAt(s3,a1)
					return _hx_local_23
			elif (field == "substr"):
				if isinstance(o,str):
					s8 = o
					def _hx_local_24(a14):
						return HxString.substr(s8,a14)
					return _hx_local_24
			elif (field == "filter"):
				if isinstance(o,list):
					x5 = o
					def _hx_local_25(f1):
						return python_internal_ArrayImpl.filter(x5,f1)
					return _hx_local_25
			elif (field == "concat"):
				if isinstance(o,list):
					a16 = o
					def _hx_local_26(a21):
						return python_internal_ArrayImpl.concat(a16,a21)
					return _hx_local_26
			elif (field == "insert"):
				if isinstance(o,list):
					a3 = o
					def _hx_local_27(a17,x8):
						python_internal_ArrayImpl.insert(a3,a17,x8)
					return _hx_local_27
			elif (field == "remove"):
				if isinstance(o,list):
					x13 = o
					def _hx_local_28(e2):
						return python_internal_ArrayImpl.remove(x13,e2)
					return _hx_local_28
			elif (field == "splice"):
				if isinstance(o,list):
					x17 = o
					def _hx_local_29(a19,a22):
						return python_internal_ArrayImpl.splice(x17,a19,a22)
					return _hx_local_29
		else:
			pass
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def getInstanceFields(c):
		f = None
		if hasattr(c,"_hx_fields"):
			f = c._hx_fields
		else:
			f = []
		if hasattr(c,"_hx_methods"):
			a = c._hx_methods
			f = (f + a)
		sc = python_Boot.getSuperClass(c)
		if (sc is None):
			return f
		else:
			scArr = python_Boot.getInstanceFields(sc)
			scMap = set(scArr)
			res = []
			_g = 0
			while (_g < len(f)):
				f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
				_g = (_g + 1)
				if (not f1 in scMap):
					scArr.append(f1)
			return scArr

	@staticmethod
	def getSuperClass(c):
		if (c is None):
			return None
		try:
			if hasattr(c,"_hx_super"):
				return c._hx_super
			return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		return None

	@staticmethod
	def getClassFields(c):
		if hasattr(c,"_hx_statics"):
			x = c._hx_statics
			return list(x)
		else:
			return []

	@staticmethod
	def unhandleKeywords(name):
		if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
			real = HxString.substr(name,python_Boot.prefixLength,None)
			if real in python_Boot.keywords:
				return real
		return name


class python_HaxeIterator:
	_hx_class_name = "python.HaxeIterator"
	_hx_fields = ["it", "x", "has", "checked"]
	_hx_methods = ["next", "hasNext"]

	def __init__(self,it):
		self.it = None
		self.x = None
		self.has = None
		self.checked = None
		self.checked = False
		self.has = False
		self.x = None
		self.it = it

	def next(self):
		if (not self.checked):
			self.hasNext()
		self.checked = False
		return self.x

	def hasNext(self):
		if (not self.checked):
			try:
				self.x = self.it.__next__()
				self.has = True
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					self.has = False
					self.x = None
				else:
					raise _hx_e
			self.checked = True
		return self.has



class python_Lib:
	_hx_class_name = "python.Lib"
	_hx_statics = ["dictToAnon"]

	@staticmethod
	def dictToAnon(v):
		return _hx_AnonObject(v.copy())


class python_internal_ArrayImpl:
	_hx_class_name = "python.internal.ArrayImpl"
	_hx_statics = ["get_length", "concat", "iterator", "indexOf", "lastIndexOf", "toString", "pop", "push", "unshift", "remove", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get"]

	@staticmethod
	def get_length(x):
		return len(x)

	@staticmethod
	def concat(a1,a2):
		return (a1 + a2)

	@staticmethod
	def iterator(x):
		return python_HaxeIterator(x.__iter__())

	@staticmethod
	def indexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		l = None
		if (fromIndex is None):
			l = 0
		elif (fromIndex < 0):
			l = (_hx_len + fromIndex)
		else:
			l = fromIndex
		if (l < 0):
			l = 0
		_g = l
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			if (a[i] == x):
				return i
		return -1

	@staticmethod
	def lastIndexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		l = None
		if (fromIndex is None):
			l = _hx_len
		elif (fromIndex < 0):
			l = ((_hx_len + fromIndex) + 1)
		else:
			l = (fromIndex + 1)
		if (l > _hx_len):
			l = _hx_len
		def _hx_local_1():
			nonlocal l
			l = (l - 1)
			return l
		while (_hx_local_1() > -1):
			if (a[l] == x):
				return l
		return -1

	@staticmethod
	def toString(x):
		return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

	@staticmethod
	def pop(x):
		if (len(x) == 0):
			return None
		else:
			return x.pop()

	@staticmethod
	def push(x,e):
		x.append(e)
		return len(x)

	@staticmethod
	def unshift(x,e):
		x.insert(0, e)

	@staticmethod
	def remove(x,e):
		try:
			x.remove(e)
			return True
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e1 = _hx_e1
			return False

	@staticmethod
	def shift(x):
		if (len(x) == 0):
			return None
		return x.pop(0)

	@staticmethod
	def slice(x,pos,end = None):
		return x[pos:end]

	@staticmethod
	def sort(x,f):
		x.sort(key= python_lib_Functools.cmp_to_key(f))

	@staticmethod
	def splice(x,pos,_hx_len):
		if (pos < 0):
			pos = (len(x) + pos)
		if (pos < 0):
			pos = 0
		res = x[pos:(pos + _hx_len)]
		del x[pos:(pos + _hx_len)]
		return res

	@staticmethod
	def map(x,f):
		return list(map(f,x))

	@staticmethod
	def filter(x,f):
		return list(filter(f,x))

	@staticmethod
	def insert(a,pos,x):
		a.insert(pos, x)

	@staticmethod
	def reverse(a):
		a.reverse()

	@staticmethod
	def _get(x,idx):
		if ((idx > -1) and ((idx < len(x)))):
			return x[idx]
		else:
			return None


class _HxException(Exception):
	_hx_class_name = "_HxException"
	_hx_fields = ["val"]
	_hx_methods = []
	_hx_statics = []
	_hx_super = Exception


	def __init__(self,val):
		self.val = None
		message = str(val)
		super().__init__(message)
		self.val = val



class HxOverrides:
	_hx_class_name = "HxOverrides"
	_hx_statics = ["eq", "stringOrNull"]

	@staticmethod
	def eq(a,b):
		if (isinstance(a,list) or isinstance(b,list)):
			return a is b
		return (a == b)

	@staticmethod
	def stringOrNull(s):
		if (s is None):
			return "null"
		else:
			return s


class HxString:
	_hx_class_name = "HxString"
	_hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "toString", "get_length", "substring", "substr"]

	@staticmethod
	def split(s,d):
		if (d == ""):
			return list(s)
		else:
			return s.split(d)

	@staticmethod
	def charCodeAt(s,index):
		if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
			return None
		else:
			return ord(s[index])

	@staticmethod
	def charAt(s,index):
		if ((index < 0) or ((index >= len(s)))):
			return ""
		else:
			return s[index]

	@staticmethod
	def lastIndexOf(s,_hx_str,startIndex = None):
		if (startIndex is None):
			return s.rfind(_hx_str, 0, len(s))
		else:
			i = s.rfind(_hx_str, 0, (startIndex + 1))
			startLeft = None
			if (i == -1):
				startLeft = max(0,((startIndex + 1) - len(_hx_str)))
			else:
				startLeft = (i + 1)
			check = s.find(_hx_str, startLeft, len(s))
			if ((check > i) and ((check <= startIndex))):
				return check
			else:
				return i

	@staticmethod
	def toUpperCase(s):
		return s.upper()

	@staticmethod
	def toLowerCase(s):
		return s.lower()

	@staticmethod
	def indexOf(s,_hx_str,startIndex = None):
		if (startIndex is None):
			return s.find(_hx_str)
		else:
			return s.find(_hx_str, startIndex)

	@staticmethod
	def toString(s):
		return s

	@staticmethod
	def get_length(s):
		return len(s)

	@staticmethod
	def substring(s,startIndex,endIndex = None):
		if (startIndex < 0):
			startIndex = 0
		if (endIndex is None):
			return s[startIndex:]
		else:
			if (endIndex < 0):
				endIndex = 0
			if (endIndex < startIndex):
				return s[endIndex:startIndex]
			else:
				return s[startIndex:endIndex]

	@staticmethod
	def substr(s,startIndex,_hx_len = None):
		if (_hx_len is None):
			return s[startIndex:]
		else:
			if (_hx_len == 0):
				return ""
			return s[startIndex:(startIndex + _hx_len)]

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

PieChartGen.SIZE = 300
PieChartGen.RADIUS = 130
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")