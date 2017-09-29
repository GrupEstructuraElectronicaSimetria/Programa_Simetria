def reading_input(input_name, molecules, names):

    coord = []
    elements = []
    i = -1
    with open(input_name) as lines:
        for line in lines:
            if '#' in line:
                names.append(line[1:])
                i = i + 1
                if i > 0:
                    molecules['geom' + str(i)] = [elements] + [coord]
                coord = []
                elements = []
            else:
                list1 = line.split()
                elements.append(list1[0])
                coord.append([float(i) for i in list1[1:]])

    try:
        int(elements[0])
        ele = []
        for number in elements:
            ele.append(atomic_elements[int(number)-1])
        elements = ele
    except ValueError:
        pass

    molecules['geom' + str(i+1)] = [elements] + [coord]


atomic_elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
                   'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga',
                   'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
                   'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
                   'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os',
                   'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
                   'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs']
