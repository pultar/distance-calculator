import pytest
import numpy as np

from distance import distance_naive, distance_numpy, distance_pygromos
from pygromos.files.coord.cnf import Cnf

ACCURACY = 10 ** -7

EXAMPLE_FILE = "examples/menthol.cnf"

DISTANCES_REF = [
  0.10900251779675933,
  3.008038939682372,
  2.9829131968815035
]

TEST_DISTANCES_BY_ATOM = [
    (0,  1,  DISTANCES_REF[0], 0),
    (0,  20, DISTANCES_REF[1], 0),
    (20, 30, DISTANCES_REF[2], 0),
    (1,  2,  DISTANCES_REF[0], 1),
    (1,  21, DISTANCES_REF[1], 1),
    (21, 31, DISTANCES_REF[2], 1)
]

TEST_DISTANCES_BY_NUMPY = [
    (np.array([3.003313233, 0.582196780, 1.245597529]), np.array([2.908414969, 0.625432521, 1.213871529]),  DISTANCES_REF[0]), # atom 0 -> atom 1
    (np.array([3.003313233, 0.582196780, 1.245597529]), np.array([0.058406294, 0.862609252, 1.790749094]),  DISTANCES_REF[1]), # atom 0 -> atom 20
    (np.array([0.058406294, 0.862609252, 1.790749094]), np.array([3.000860882, 0.419008917, 1.583503152]),  DISTANCES_REF[2]) # atom 20 -> atom 30
]

@pytest.mark.parametrize("atom_1, atom_2, distance", TEST_DISTANCES_BY_NUMPY)
def test_distance_naive(atom_1, atom_2, distance):
    assert pytest.approx(distance_naive(atom_1, atom_2), ACCURACY) == distance

@pytest.mark.parametrize("atom_1, atom_2, distance", TEST_DISTANCES_BY_NUMPY)
def test_distance_numpy(atom_1, atom_2, distance):
    assert pytest.approx(distance_numpy(atom_1, atom_2), ACCURACY) == distance

@pytest.mark.parametrize("atom_1, atom_2, distance, idx_start", TEST_DISTANCES_BY_ATOM)
def test_distance_pygromos(atom_1, atom_2, distance, idx_start):
    my_configuration = Cnf(EXAMPLE_FILE)
    assert pytest.approx(distance_pygromos(my_configuration, atom_1, atom_2, idx=idx_start), ACCURACY) == distance

