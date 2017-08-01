def hellOnEarth():

    for index in range(100, 100001):
        prime = True
        square = False
        count = 2

        while ( count * count <= index):
            if (count * count == index):
                print "Bar ", index
                square = True
                break
            elif (index % count == 0):
                prime = False
                break
            count += 1
        if prime == True :
            print "Foo ", index
        elif square != True:
            print "FooBar"

hellOnEarth()