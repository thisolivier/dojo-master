print "\n-------\n Odd or Even? \n-------\n"

def oddEven() :
    for val in range(1, 2001):
        oddEvenStr = "odd number."
        if (val % 2 == 0):
            oddEvenStr = "even number."
        print "Number is " + str(val) + ". This is an", oddEvenStr

oddEven()

print "\n-------\n Multiply the list Values \n-------\n"

def multiply(list, num) :
    returnVal = []
    for val in list:
        returnVal.append(val * num)
    return returnVal

a = [2,4,10,16]
b = multiply(a, 5)
print b

print "\n-------\n Why even try to explain this? \n-------\n"

def multiplyRevenge(list) :
    returnVal = []
    for val in list :
        fruity = [1] * val
        returnVal.append(fruity)
    return returnVal

x = multiplyRevenge(multiply([2,4,5],3))
print x