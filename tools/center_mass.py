import numpy as np


def get_mass(elements):
    mass_vector = []
    for i in elements:
        mass_vector.append(float(atom_prop[i.capitalize()][1]))
    return mass_vector


def get_v_cm(elements, coord):
    mass_vector = get_mass(elements)
    cbye = [np.dot(mass_vector[i], coord[i]) for i in range(len(elements))]
    r = np.sum(cbye, axis=0)
    r = r/np.sum(mass_vector)
    return r

atom_prop = dict(H=['1', '1.0079', 'Hydrogen'], He=['2', '4.0026', 'Helium'], Li=['3', '6.941', 'Lithium'],
                 Be=['4', '9.0122', 'Beryllium'], B=['5', '10.811', 'Boron'], C=['6', '12.0107', 'Carbon'],
                 N=['7', '14.0067', 'Nitrogen'], O=['8', '15.9994', 'Oxygen'], F=['9', '18.9984', 'Fluorine'],
                 Ne=['10', '20.1797', 'Neon'], Na=['11', '22.9897', 'Sodium'], Mg=['12', '24.305', 'Magnesium'],
                 Al=['13', '26.9815', 'Aluminum'], Si=['14', '28.0855', 'Silicon'], P=['15', '30.9738', 'Phosphorus'],
                 S=['16', '32.065', 'Sulfur'], Cl=['17', '35.453', 'Chlorine'], K=['19', '39.0983', 'Potassium'],
                 Ar=['18', '39.948', 'Argon'], Ca=['20', '40.078', 'Calcium'], Sc=['21', '44.9559', 'Scandium'],
                 Ti=['22', '47.867', 'Titanium'], V=['23', '50.9415', 'Vanadium'], Cr=['24', '51.9961', 'Chromium'],
                 Mn=['25', '54.938', 'Manganese'], Fe=['26', '55.845', 'Iron'], Ni=['28', '58.6934', 'Nickel'],
                 Co=['27', '58.9332', 'Cobalt'], Cu=['29', '63.546', 'Copper'], Zn=['30', '65.39', 'Zinc'],
                 Ga=['31', '69.723', 'Gallium'], Ge=['32', '72.64', 'Germanium'], As=['33', '74.9216', 'Arsenic'],
                 Se=['34', '78.96', 'Selenium'], Br=['35', '79.904', 'Bromine'], Kr=['36', '83.8', 'Krypton'],
                 Rb=['37', '85.4678', 'Rubidium'], Sr=['38', '87.62', 'Strontium'], Y=['39', '88.9059', 'Yttrium'],
                 Zr=['40', '91.224', 'Zirconium'], Nb=['41', '92.9064', 'Niobium'], Mo=['42', '95.94', 'Molybdenum'],
                 Tc=['43', '98', 'Technetium'], Ru=['44', '101.07', 'Ruthenium'], Rh=['45', '102.9055', 'Rhodium'],
                 Pd=['46', '106.42', 'Palladium'], Ag=['47', '107.8682', 'Silver'], Cd=['48', '112.411', 'Cadmium'],
                 In=['49', '114.818', 'Indium'], Sn=['50', '118.71', 'Tin'], Sb=['51', '121.76', 'Antimony'],
                 I=['53', '126.9045', 'Iodine'], Te=['52', '127.6', 'Tellurium'], Xe=['54', '131.293', 'Xenon'],
                 Cs=['55', '132.9055', 'Cesium'], Ba=['56', '137.327', 'Barium'], La=['57', '138.9055', 'Lanthanum'],
                 Ce=['58', '140.116', 'Cerium'], Pr=['59', '140.9077', 'Praseodymium'],
                 Nd=['60', '144.24', 'Neodymium'], Pm=['61', '145', 'Promethium'], Sm=['62', '150.36', 'Samarium'],
                 Eu=['63', '151.964', 'Europium'], Gd=['64', '157.25', 'Gadolinium'], Tb=['65', '158.9253', 'Terbium'],
                 Dy=['66', '162.5', 'Dysprosium'], Ho=['67', '164.9303', 'Holmium'], Er=['68', '167.259', 'Erbium'],
                 Tm=['69', '168.9342', 'Thulium'], Yb=['70', '173.04', 'Ytterbium'], Lu=['71', '174.967', 'Lutetium'],
                 Hf=['72', '178.49', 'Hafnium'], Ta=['73', '180.9479', 'Tantalum'], W=['74', '183.84', 'Tungsten'],
                 Re=['75', '186.207', 'Rhenium'], Os=['76', '190.23', 'Osmium'], Ir=['77', '192.217', 'Iridium'],
                 Pt=['78', '195.078', 'Platinum'], Au=['79', '196.9665', 'Gold'], Hg=['80', '200.59', 'Mercury'],
                 Tl=['81', '204.3833', 'Thallium'], Pb=['82', '207.2', 'Lead'], Bi=['83', '208.9804', 'Bismuth'],
                 Po=['84', '209', 'Polonium'], At=['85', '210', 'Astatine'], Rn=['86', '222', 'Radon'],
                 Fr=['87', '223', 'Francium'], Ra=['88', '226', 'Radium'], Ac=['89', '227', 'Actinium'],
                 Pa=['91', '231.0359', 'Protactinium'], Th=['90', '232.0381', 'Thorium'], Np=['93', '237', 'Neptunium'],
                 U=['92', '238.0289', 'Uranium'], Am=['95', '243', 'Americium'], Pu=['94', '244', 'Plutonium'],
                 Cm=['96', '247', 'Curium'], Bk=['97', '247', 'Berkelium'], Cf=['98', '251', 'Californium'],
                 Es=['99', '252', 'Einsteinium'], Fm=['100', '257', 'Fermium'], Md=['101', '258', 'Mendelevium'],
                 No=['102', '259', 'Nobelium'], Rf=['104', '261', 'Rutherfordium'], Lr=['103', '262', 'Lawrencium'],
                 Db=['105', '262', 'Dubnium'], Bh=['107', '264', 'Bohrium'], Sg=['106', '266', 'Seaborgium'],
                 Mt=['109', '268', 'Meitnerium'], Rg=['111', '272', 'Roentgenium'], Hs=['108', '277', 'Hassium'])
