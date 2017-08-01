import random

def grade_killer () :
    for val in range(0,10):
        grade = random.randint(60, 101)
        begin_string = "Score: " + str(grade) + "; Your grade is "
        if grade < 70 :
            print begin_string + "D"
        elif grade < 80:
            print begin_string + "C"
        elif grade < 90:
            print begin_string + "B"
        else:
            print begin_string + "A"

grade_killer()