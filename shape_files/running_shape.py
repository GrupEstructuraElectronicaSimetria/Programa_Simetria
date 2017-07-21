# Shape functions in progress...
from subprocess import Popen, PIPE
import os.path
import time


# shape_files input
def shape_input(name, n_atoms, coord, elements, reference,
                central_atom=0):
    f = open(name + '.dat', 'w')
    f.write('$ ' + name)
    f.write('\n')
    f.write('! vertexes central_atom')
    f.write('\n')
    if central_atom != 0:
        f.write(str(n_atoms - 1) + ' ' + str(central_atom))
    else:
        f.write(str(n_atoms) + ' ' + str(central_atom))
    f.write('\n')
    f.write('! ideal structure')
    f.write('\n')
    f.write(reference)
    f.write('\n')
    f.write('example')
    f.write('\n')

    for i in range(n_atoms):
        f.write('{0:5} {1:6}'.format(elements[i],
                                     ' '.join(map(str, coord[i]))))
        f.write('\n')
    f.close()


# Run shape_files from py
def run_shape(name):
    Popen(["./shape_macox", name], stdout=PIPE)


def references():
    proc = Popen(['./shape_macox', '+2'], stdout=PIPE)
    out = []
    for line in proc.stdout:
        print(line.decode('utf-8'))
        out.append(line.decode('utf-8').splitlines())
    reference = input('Which reference do you want? ')
    return reference


def read_output(output):
    while not os.path.exists('test.tab'):
         time.sleep(0.1)
    with open(output+'.tab') as lines:
        for line in lines:
            if 'example' in line:
                list1 = line.split()
                percentage = list1[-1]
                return percentage
