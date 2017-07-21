import running_shape


name = 'test'
class Shape:

    def __init__(self, n_atoms, structure, elements, central_atom=0):
        self.set_number(n_atoms, structure, elements, central_atom)

    def set_number(self, n_atoms, structure, elements, central_atom):
        reference = running_shape.references()
        running_shape.shape_input(name, n_atoms, structure, elements,
                                  reference, central_atom)
        self.run_shape()
        self._percentatge = running_shape.read_output(name)

    def get_number(self):
        return self._percentatge

    def run_shape(self):
        running_shape.run_shape(name)
