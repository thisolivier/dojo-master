def theMultiplyer():
    for col in range(1, 13):
        col2 = col - 1
        if col == 1:
            col2 = 'x'
        list = [col2]
        for row in range(1, 13):
            list.append(str(row * col).zfill(3))
        print ' '.join(map(str, list))


theMultiplyer()
