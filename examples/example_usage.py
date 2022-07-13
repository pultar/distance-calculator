from pygromos.files.coord.cnf import Cnf
from gdist import distance_numpy as calc_dist_1
from gdist import distance_pygromos as calc_dist_2

import numpy as np

array_1 = np.random.rand(3)
array_2 = np.random.rand(3)

print(array_1)
print(array_2)

distance_1 = calc_dist_1(array_1, array_2)
print(f"Distance calculated from random arrays: {distance_1}")

my_configuration = Cnf("menthol.cnf")
coord = my_configuration.get_atom_coordinates()

# indices can start from 0 and 1, a switch is only supported within PyGromosTools
atom_1_0 = 0
atom_2_0 = 1
atom_1_1 = 1
atom_2_1 = 2

# demonstrate 0-based and 1-based methods
distance_numpy = calc_dist_1(coord[atom_1_0], coord[atom_2_0])
distance_pygromos_0_based = calc_dist_2(my_configuration, atom_1_0, atom_2_0, idx=0)
distance_pygromos_1_based = calc_dist_2(my_configuration, atom_1_1, atom_2_1, idx=1)
print(f"Distance calculated between atoms {atom_1_0} and {atom_2_0} for menthol.cnf (0-based): {distance_numpy} nm")
print(f"Distance calculated between atoms {atom_1_0} and {atom_2_0} for menthol.cnf (0-based): {distance_pygromos_0_based} nm")
print(f"Distance calculated between atoms {atom_1_1} and {atom_2_1} for menthol.cnf (1-based): {distance_pygromos_1_based} nm")
