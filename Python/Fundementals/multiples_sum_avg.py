print ''
print '###############'
print 'List Lots'
print ''
# So, here we list the odd numbers form 1 to 1000
# Modulo is used to check is a number if odd

def listLots():
    for ind in range(1, 1000):
        if (ind % 2) != 0:
            print ind

listLots()

print ''
print '###############'
print 'Sum List'
print ''

def sumList(list):
    sum = 0
    for val in list:
        sum += val
    return sum

print sumList(list = [1, 2, 5, 10, 255, 3])

print ''
print '###############'
print 'Average List'
print ''

def avgList(list):
    sum = float(sumList(list))
    length = float(len(list))
    return sum / length

print avgList(list = [1, 2, 5, 10, 255, 3])