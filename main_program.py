from molecule import Molecule
from inout import read
from shape_files import shape


# Ini variables
input_name = 'example01.inp'
molecules = {}
names = []

# Reading input file
read.reading_input(input_name, molecules, names)

# Create objects
H2O = Molecule(molecules["geom1"][1], molecules["geom1"][0], True)
list_frag = [[0, 2]]
frag1 = Molecule.Geometry(molecules["geom1"][1])
test2 = frag1.get_fragment()

# Create an input for shape_files and run the program
test = shape.Shape(H2O.get_n_atoms(), H2O.get_coord(),
                   H2O.get_elements(), 1)
print(test.get_number())
