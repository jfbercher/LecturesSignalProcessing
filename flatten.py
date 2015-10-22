#Flattening a list of list
#from http://rightfootin.blogspot.fr/2006/09/more-on-python-flatten.html which derives
#from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/363051
def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

flatten(lw)