import ipdb

class Scale:

    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'
    G = 'g'

    B_FLAT = 'b_flat'
    E_FLAT = 'e_flat'
    A_FLAT = 'a_flat'
    D_FLAT = 'd_flat'
    G_FLAT = 'g_flat'

    WHICH = MappingProxyType({
        C: (SHARPS, 0)
        G: (SHARPS, 1)
        D: (SHARPS, 2)
        A: (SHARPS, 3)
        E: (SHARPS, 4)
        B: (SHARPS, 5)
        F: (FLATS, 1)
        B_FLAT: (FLATS, 2)
        E_FLAT: (FLATS, 3)
        A_FLAT: (FLATS, 4)
        D_FLAT: (FLATS, 5)
        G_FLAT: (FLATS, 6)
        })

    FLATS = (B, E, A, D, G, C, F)
    SHARPS = tuple(reversed(FLATS))

    __slots__ = ('root',)

    def __init__(self, root):
        self.root = root

    def notes(self):
        flats = list(sorted(self.FLATS))
        index = flats.index(self.root)
        first = flats[index:]
        last = flats[:index]
        return first + last


if __name__ == '__main__':
    print(Scale('a').notes())
    print(Scale('b').notes())
    print(Scale('c').notes())
    print(Scale('d').notes())
    print(Scale('e').notes())
    print(Scale('f').notes())
    print(Scale('g').notes())
