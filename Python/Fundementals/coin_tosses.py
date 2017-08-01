import random

def coin_program():

        headTot = 0
        tailTot = 0
        print "Starting the program..."
        for index in range(1, 5001):
            if int(round(random.random())) :
                tailTot += 1
                resultString = "tail"
            else :
                headTot += 1
                resultString = "head"
            print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(index, resultString, headTot, tailTot)

coin_program()