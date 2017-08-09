class UserDB (object):
    def __init__ (self):
        self.data = []
        self.idCount = 0
    
    def create(self, name, age):
        self.idCount += 1
        self.data.append( User(name, age, self.idCount, self) )
        return self

    def all(self):
        return self.data

    def get(self, name):
        for user in self.data :
            if user.name == name :
                return user
        return False
    
    def filter(self, name):
        returnList = []
        for user in self.data :
            if user.name == name :
                returnList.append(user)
        return returnList

    def exclude(self, name):
        returnList = []
        for user in self.data :
            if user.name != name :
                returnList.append(user)
        return returnList
    
    def delete(self, name):
        for user in self.data :
            if user.name == name :
                self.data.remove(user)
        return self

class User (object):
    def __init__ (self, newName, newAge, newId, originDB):
        self.name = newName
        self.age = newAge
        self.id = newId
        self.db = originDB

    def __repr__ (self):
        return '< User ID{} name:{} age:{} >'.format(self.id, self.name, self.age)

    def save(self):
        for user in self.db.data:
            if user.id == self.id:
                user = self
                return True
        return False

myDB = UserDB()
myDB.create('Joe','102').create('Lil Timmy','2').create('Joe','33')
print myDB.all()

x = myDB.get('Joe')
x.name = 'Hubert Hump'
x.save()

print myDB.all()
