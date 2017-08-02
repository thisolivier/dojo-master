class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = {}
        self.name = str(name)
        self.capacity = int(capacity)
    
    def admit(self, name, allergies):
        bedNo = None
        for index in range(0,self.capacity) :
            if not (index in self.patients) : 
                bedNo = index
                break
        
        if bedNo == None : 
            print "\n--------\nError - No beds free\nList of current patients as follows\n--------"
            self.whoSick()
        else :
            newPatient = Patient(name, allergies, bedNo)
            self.patients[bedNo] = newPatient
        return self
    
    def discharge(self, name):
        for key in self.patients :
            maybeBetter = self.patients[key]
            if maybeBetter.name == name:
                self.patients[key].bed = None
                self.patients.pop(key)
                break
        return self

    def whoSick(self):
        print "\n--------\nPatients at {} Hospital\n--------".format(self.name)
        for key in self.patients :
            sickOne = self.patients[key]
            print "- - - - -\n{}\n- - - - -".format(sickOne.name)
            print "Allergies:",sickOne.allergies
            print "Patient ID:",sickOne.patientID
            print "Bed Number:", sickOne.bed
        return self



class Patient(object):
    count = 0
    def __init__(self, name, allergies, bed = None):
        self.name = name
        self.allergies = allergies
        self.bed = bed
        self.patientID = self.count
        self.count += 1

oopsHospital = Hospital("Sweet Love", 3)
oopsHospital.admit("Johnny", "All work no play").admit("Superman","kryptonite").admit("Lex Luthor","superman")
oopsHospital.discharge("Superman").admit("Shreck","Other people").whoSick()