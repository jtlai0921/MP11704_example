def demo(jitu, tui):
    tu = (tui - jitu*2) / 2
    if int(tu) == tu:
        return (int(jitu-tu), int(tu))

print(demo(30, 90))
