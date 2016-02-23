def histo(file):
    f = open(file)
    heading=None
    x,y=[],[]
    for line in f:
        if line.startswith("#"):
            continue
        wd=line.split(" ")
        if not heading: #heading not defined
            heading=wd
        else:
            x.append(wd[1])
            y.append(wd[3])
    f.close()
    x = np.array(map(float,x))
    y = np.array(map(float,y))
    return x,y
