def print_magic(list):
    for things in list:
        if str(type(things)).find('str') >= 0:
            noStars = len(things)
            stars = things[0].lower()
        else :
            noStars = things
            stars = "*"

        print stars * noStars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print_magic(list = x)