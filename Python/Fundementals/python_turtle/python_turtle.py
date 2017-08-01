import turtle

DIST = 10
for x in range(0,12):
    print "x", x
    turtle.right(20)
    for y in range(0,9):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(70 / (y+1))
        # advance according to set distance
        turtle.forward(DIST)
        if (y % 3 == 0):
            turtle.left(90)
            turtle.forward(DIST/5)
            turtle.right(90)
            turtle.forward(DIST / 5)
            turtle.right(90)
            turtle.forward(DIST / 5)
            turtle.left(90)
    # add to set distance
    DIST += 10