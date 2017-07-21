def reading_input(input_name, molecules, names):

    coord = []
    elements = []
    i = -1
    with open(input_name) as lines:
        for line in lines:
            if '#' in line:
                list1 = line.split()
                names.append(list1[1])
                i = i + 1
                if i > 0:
                    molecules['geom' + str(i)] = [elements] + [coord]
                coord = []
                elements = []
            else:
                list1 = line.split()
                elements.append(list1[0])
                coord.append([float(i) for i in list1[1:]])
    molecules['geom' + str(i+1)] = [elements] + [coord]
