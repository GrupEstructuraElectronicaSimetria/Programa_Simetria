import numpy as np
import center_mass


class Molecule:
    def __init__(self, coord, elements, cm=True):
        self.set_elements(elements)
        self._coord = np.array(coord)
        self.set_coord(coord)
        self.get_n_atoms()

    def get_elements(self):
        return self._elements

    def set_elements(self, elements):
        self._elements = [x.capitalize() for x in elements]

    def set_coord(self, coord):
        r = center_mass.get_v_cm(self._elements, coord)
        self._cent_mass = r
        coord_cm = coord - self._cent_mass
        self._cent_coord = np.array(coord_cm)

    def get_coord(self):
        return self._coord

    def get_cent_coord(self):
        return self._cent_coord

    def get_n_atoms(self):
        natoms = len(self._elements)
        return natoms

    def get_cent_mass(self):
        return self._cent_mass


    class Geometry:

        def __init__(self, coord, frag=0):
            self.set_fragment(coord, frag)

        def get_fragment(self):
            return self._coord

        def set_fragment(self, coord, frag):
            if frag == 0:
                self._coord = np.array(coord)
            else:
                fragment = []
                for i in list(map(int, frag)):
                    fragment.append(coord[i])
                self._coord = np.array(fragment)
