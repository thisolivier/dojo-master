def type_chaos(list):
    bools = [False, False]
    newStr = ""
    newint = 0
    for value in list:
        theType = type(value).__name__
        if theType == 'str':
            bools[0] = True
            newStr += " " + value
        elif theType == 'int':
            bools[1] = True
            newint += value
        else:
            print "Unexpected value in list; ", value

    if bools[0] and bools[1]:
        print "You passed us a mixed list"
        print "the combined string is ", newStr
        print "The new number is ", newint
    elif bools[0]:
        print "That was a list of strings"
        print "Concatinated strings as follows; ", newStr
    elif bools[1]:
        print "That was a list of numbers"
        print "Summed to; ", newint
    else:
        print "Not at all correct"

type_chaos(list = ['magical','unicorns'])