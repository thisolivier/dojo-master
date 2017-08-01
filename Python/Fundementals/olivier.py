def build_Horror():
    x = {"Olivier":"awesome"}
    y = {"Body":"lumpy"}
    z = (x,y)
    print z
    x["Olivier"] = "bingo cool"
    print z
    del y
    print z

build_Horror()