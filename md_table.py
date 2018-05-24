def maker(col, row, alignment="left"):
    verts = "|    "
    for i in range(col):
        print(verts, end=' ')
    print(verts)
    for i in range(col):
        if alignment == "right":
            bar = "|----:"
        elif alignment == "centre":
            bar = "|:---:"
        else:
            bar = "|:----"
        print(bar, end='')
    print(verts)
    for i in range(row):
        for i in range(col):
            print(verts, end=' ')
        print("|")
