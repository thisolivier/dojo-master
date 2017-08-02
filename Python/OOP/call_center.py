from datetime import datetime
from random import shuffle

class Call(object):
    counter = 0
    def __init__(self, name, tel, reason="None given"):
        self.marker = Call.counter
        Call.counter += 1
        self.time = datetime.now()
        self.tel = tel
        self.name = name
        self.reason = reason

    def display(self):
        print "\n-----------\nCall {} details incoming\n- - - - - -\n".format(self.marker)
        print "Call ID:", self.marker
        print "Date and Time of call:", self.time
        print "Caller number:", str(self.tel)
        print "Caller name:", self.name
        print "Reason for call:", self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize = 0

    def updateList(self):
        self.queueSize = len(self.calls)
        return self

    def add(self, name, tel, reason="None given"):
        self.calls.append( Call(name, tel, reason) )
        self.updateList()
        return self

    def remove(self, tel=False):
        index = 0
        if tel :
            found = False
            for ind, val in enumerate(self.calls):
                if val.tel == str(tel): 
                    index = ind
                    found = True
                break
            if not found : 
                print "\n-----------\nFail - No matching telephone for {}\n-----------\n".format(tel)
                return self
        
        self.calls.pop(index)
        self.updateList()
        return self

    def infoPrint(self):
        print "\n-----------\nDetails incoming for call queue (length {})\n-----------".format(self.queueSize)
        for val in self.calls:
            val.display()
        return self

    def shuffleMe(self):
        shuffle(self.calls)
        return self

    def emergencyReset(self):
        for ind, val in enumerate(self.calls):
            tempMin = None
            indexMin = None
            print "The main index is",ind
            for ind2, val2 in enumerate(self.calls):
                if (ind2 >= ind) and ((tempMin == None) or (val2.time < tempMin)):
                    print "The secondary index is",ind2
                    tempMin = val2.time
                    indexMin = ind2
            
            if not indexMin == ind:
                temp = self.calls[indexMin]
                self.calls[indexMin] = self.calls[ind]
                self.calls[ind] = temp
        return self

boringCompany = CallCenter()
boringCompany.add("Aquaman", "000").add("Bill G", "0000").add("Batman", "1234").add("Treebeard", "4321").infoPrint()
boringCompany.shuffleMe().infoPrint().emergencyReset().infoPrint()