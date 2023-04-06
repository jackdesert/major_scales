from types import MappingProxyType
import random
from datetime import datetime
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

    FLATS = (B, E, A, D, G, C, F)
    SHARPS = tuple(reversed(FLATS))
    KEYS = tuple([A, B, C, D, E, F, G, B_FLAT, E_FLAT, A_FLAT, D_FLAT, G_FLAT])

    WHICH = MappingProxyType({
        C: (SHARPS, 0),
        G: (SHARPS, 1),
        D: (SHARPS, 2),
        A: (SHARPS, 3),
        E: (SHARPS, 4),
        B: (SHARPS, 5),
        F: (FLATS, 1),
        B_FLAT: (FLATS, 2),
        E_FLAT: (FLATS, 3),
        A_FLAT: (FLATS, 4),
        D_FLAT: (FLATS, 5),
        G_FLAT: (FLATS, 6),
        })


    __slots__ = ('root',)

    def __init__(self, root):
        self.root = root

    def _notes_raw(self):
        flats = list(sorted(self.FLATS))
        index = flats.index(self.root[:1])
        first = flats[index:]
        last = flats[:index]
        return first + last

    def notes(self):
        raw = self._notes_raw()
        flats_or_sharps, num_accidentals = self.WHICH[self.root]
        accidentals = flats_or_sharps[:num_accidentals]
        accidental = '#' if flats_or_sharps == self.SHARPS else 'b'
        output = []
        for note in raw:
            if note in accidentals:
                output.append(f'{note}{accidental}'.upper())
            else:
                output.append(note.upper())
        return output

def list_all():
    print(Scale('a').notes())
    print(Scale('b').notes())
    print(Scale('c').notes())
    print(Scale('d').notes())
    print(Scale('e').notes())
    print(Scale('f').notes())
    print(Scale('g').notes())


class Asker:
    @classmethod
    def ask_all(cls):
        start = datetime.now()
        keys = list(Scale.KEYS)
        random.shuffle(keys)
        for key in keys:
            while True:
                answer = input(f'Which notes are in the key of {key.upper()}? ')
                answer_list = answer.upper().strip().split(',')
                answer_list_cleaned = []
                for note in answer_list:
                    answer_list_cleaned.append(cls.format(note))
                if answer_list_cleaned == Scale(key).notes():
                    break
                else:
                    print('Try again :heart:')
        elapsed = (datetime.now() - start).total_seconds()
        print(f'You Completed all 12 scales in only {round(elapsed)} seconds')
        print('You WIN. You are WAY WAY WAY faster than Metcalf')

    @staticmethod
    def format(note):
        """
        Allow alternate spellings:

        CS -> C#
        BF -> BB
        """
        if (len(note) == 2) and note.endswith('S'):
            return f'{note[0]}#'
        return note

if __name__ == '__main__':
    Asker.ask_all()
