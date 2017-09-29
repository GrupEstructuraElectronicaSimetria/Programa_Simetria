from molecule import Molecule
from inout import read
# from shape_files import shape
import shp


#print(shp.cshm.__doc__)

# Ini variables
input_name = 'example01.inp'
molecules = {}
names = []

# Reading input file
read.reading_input(input_name, molecules, names)

# Create objects
H2O = Molecule(molecules["geom1"][1], molecules["geom1"][0], True)
coord = H2O.get_cent_coord()
#list_frag = coord[1:]
#fragment = Molecule.Geometry(H2O.get_cent_coord(), list_frag)
#print(fragment.get_fragment())

num = shp.cshm(coord, 2, True)
print(num)
print(shp.poly(coord,2, True))
print(shp.test(coord,2,True))