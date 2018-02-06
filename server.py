
def draw_stars(argu):
    newarr=[]
    for i in argu:
        cont = []
        for x in range(0, i, 1):
            cont.append(1)
        newarr.append(cont)
    return newarr
a = hacks(multiply([1,2,3],2))
print a