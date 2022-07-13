from pygromos.files.coord.cnf import Cnf
from distance import distance_numpy as calc_dist_1
from distance import distance_pygromos as calc_dist_2

import numpy as np

array_1 = np.random.rand(3)
array_2 = np.random.rand(3)

print(array_1)
print(array_2)

distance_1 = calc_dist_1(array_1, array_2)
print(f"Distance calculated from random arrays: {distance_1}")

my_configuration = Cnf("examples/menthol.cnf")
distance_2 = calc_dist_2(my_configuration, 1, 30)
print(f"Distance calculated between atoms 1 and 30 for menthol.cnf: {distance_2} nm")