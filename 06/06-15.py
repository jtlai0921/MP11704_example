def is_gif(fname):
    f = open(fname, 'r')
    first4 = tuple(f.read(4))
    f.close()
    return first4 == ('G', 'I', 'F', '8')
