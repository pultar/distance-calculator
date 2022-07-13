from distance import distance_numpy as calc_dist

import numpy as np

array_1 = np.random.rand(3)
array_2 = np.random.rand(3)

print(array_1)
print(array_2)

distance = calc_dist(array_1, array_2)
print(f"Distance calculated: {distance}")
