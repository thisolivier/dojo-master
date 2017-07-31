def whatType(unknwn):
    '''
    We could use the __name__ dunder method.
    Alternatively as we see here, I convert the type to a string,
      and then search the strings for the matching types
    '''
    theType = str(type(unknwn))

    if theType.find("str") != -1:
        if len(unknwn) >= 50:
            print "Long sentence"
        else:
            print "Small sentence"

    if theType.find('int') != -1:
        if unknwn >= 100:
            print "That's a big number"
        else:
            print "That's a small number"

    if theType.find('list') != -1:
        if len(unknwn) >= 10:
            print "Big List!"
        else:
            print "Short List..."

whatType(10000000)