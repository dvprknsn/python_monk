#05_03_converters_final
class ScaleConverter:
	
	def __init__(self, units_from, units_to, factor):
		self.units_from = units_from
		self.units_to = units_to
		self.factor = factor
#initialise the non-offset converter class with the necessary variables	
	def description(self):
		return 'Convert ' + self.units_from + ' to ' + self.units_to
#describe the conversion
	def convert(self, value):
		return value * self.factor
#method: convert 
class ScaleAndOffsetConverter(ScaleConverter):
	
	def __init__(self, units_from, units_to, factor, offset):
		ScaleConverter.__init__(self, units_from, units_to, factor)
		self.offset = offset
#inherit ScaleConverter variables
	def convert(self, value):
		return value * self.factor + self.offset
#Class: ScaleAndOffsetConverter; Method: convert
