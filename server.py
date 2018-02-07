
def draw_stars(argu):
    for i in argu:
        empt = ""
        if type(i) == str:
            z = i[0].lower()
            i = len(i)
        else:
            z = '*'
        for x in range(0, i):
            empt += z
        print empt
a = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(a)