print '###############'
print '# Find and Replace'
print ''

def findReplace(str1, str2, str3):
    position = str1.find(str2)
    print position
    finalStr = str1.replace(str2, str3, 1)
    print finalStr
    return

findReplace(str1 = "It's thanksgiving day. It's my birthday,too!", str2 = "day", str3 = "Month")

print ''
print '###############'
print '# Minimum and Max'
print ''

def minMax(listM):

    if len(listM) != 0:
        print "The minimum is", min(listM)
        print "The maximum is", max(listM)

    else :
        print "Your list is empty"
    return



minMax(listM = [2,3,19,'a',-20,2397])

print ''
print '###############'
print '# First and Last'
print ''

def firstAndLast(listM):
    listLength = len(listM)
    if listLength != 0:
        newList = [listM[0]]
        print "The first value is ", newList[0]

        last = listM[ listLength - 1 ]
        print "The last value is ", last
        newList.append(last)

        return last
    else:
        print "You gave us bad data"
        return

firstAndLast(listM = ["Hello", "Coding", "Dojo"])

print ''
print '###############'
print '# New List'
print ''

def newList(listM):
    sortedList = sorted(listM)
    listLen = len(listM)
    dividerIndex = listLen / 2
    newList = [sortedList[:dividerIndex]] + sortedList[(dividerIndex):]
    print newList

newList(listM = [19,2,54,-2,7,12,98,32,10,-3,6])