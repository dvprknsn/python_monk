#05_02_converter_offset_inheritance
class ScaleAndOffsetConverter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        ScaleConverter(self, units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return value * self.factor + self.offset

c2 = ScaleAndOffsetConverter('C', 'F', 1.8, 32)
print (c2.description())
print ('converting 20C')
print (str(c2.convert(20)) + c2.units_to)
