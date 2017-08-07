from inspect import getargspec

class Underscore(object):
    def __repr__ (self):
        return "<User object Underscore, methods map() reduce() find() filter(), helper method callCall()>"

    def callCall(self, callback, arguments):
        desiredNo = len(getargspec(callback).args)
        argSliced = arguments[0:desiredNo]
        return callback(*argSliced)

    def map (self, parList, parCall) :
        copyList = list(parList)
        returnArray = []
        for index, value in enumerate(copyList):
            argsList = [value, index, parList]
            returnArray.append(self.callCall(parCall, argsList))

        return returnArray

    def reduce (self, parList, parCall, parMemo = 0) :
        copyList = list(parList)
        for index, value in enumerate(copyList):
            argsList = [parMemo, value, index, parList]
            parMemo = self.callCall(parCall, argsList)
        return parMemo

    def find (self, parList, parCall) :
        copyList = list(parList)
        for value in copyList:
            if parCall(value) == True: 
                return value
        return None

    def filter (self, parList, parCall):
        copyList = list(parList)
        returnList = []
        for value in copyList:
            if parCall(value) == True:
                returnList.append(value)
        return returnList

    def reject (self, parList, parCall):
        copyList = list(parList)
        returnList = []
        for value in copyList:
            if parCall(value) == False:
                returnList.append(value)
        return returnList

_ = Underscore()

testFunctions = [
    lambda val, index: "Boo val {}. Index {}".format(val, index),
    lambda memo, val: memo + val,
    lambda val: True if (val % 5) == 0 else False
]

results = {
    "longer" : _.map([2,5,7], testFunctions[0]),
    "total" : _.reduce([4,5,6,2,8,10], testFunctions[1]),
    "passing" : _.find([1,2,0.3,2,155,2], testFunctions[2]),
    "filtering" : _.filter([1,5,0.3,2,155,2], testFunctions[2]),
    "rejecting" : _.reject([1,5,0.3,2,155,2], testFunctions[2]),
}

print "\n---------\nHere come the results!\n---------\n"
for key in results:
    print "{}: {}".format(key, results[key])
print ""
print _