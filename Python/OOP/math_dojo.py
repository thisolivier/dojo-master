class MathDojo(object):
    def __init__(self):
        self.counter = 0

    def add(self, *num):
        for thisNum in num:
            whatType = str(type(thisNum))
            if( whatType.find("list") >= 0 ):
                self.add(*thisNum)
            else :
                self.counter += thisNum
        return self
    
    def subtract(self, *num):
        for thisNum in num:
            whatType = str(type(thisNum))
            if( whatType.find("list") >= 0 or whatType.find("tuple") >= 0 ):
                self.subtract(*thisNum)
            else :
                self.counter -= thisNum
        return self

md = MathDojo()
md.add(24)
md.subtract((1,2,1), 10, (5,1))
print md.counter