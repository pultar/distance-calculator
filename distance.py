""" 
    Calculates the distance between two atoms in a GROMOS cnf file
    Author: Felix Pultar
    Date: July, 13 2022
"""
from pygromos.files.coord.cnf import Cnf

import sys
import numpy as np

def distance_naive(atom_1, atom_2):
    """Naive implementation using a mix of Python and numpy functions

    Args:
        atom_1 (np.array): coordinates atom_1
        atom_2 (np.array): coordinates atom_2

    Returns:
        Distance calculated
    """
    distance = np.sqrt(
      (atom_1[0] - atom_2[0]) ** 2
    + (atom_1[1] - atom_2[1]) ** 2
    + (atom_1[2] - atom_2[2]) ** 2
    )
    return distance

def distance_pygromos(atom_1, atom_2):
    """Distance calculation with PyGromosTools functionality

    Args:
        atom_1 (np.array): index atom_1 (1-based)
        atom_2 (np.array): index atom_2 (1-based)

    Returns:
        Distance calculated
    """
    distance = my_configuration.get_atoms_distance(atom_1, atom_2)
    return distance

def distance_numpy(atom_1, atom_2):
    """Implementation using only numpy functions

    Args:
        atom_1 (np.array): coordinates atom_1
        atom_2 (np.array): coordinates atom_2

    Returns:
        Distance calculated
    """
    distance = np.linalg.norm(atom_1 - atom_2)
    return distance

if __name__ == "__main__":
    usage = "usage: python main.py [path_to_cnf] [atom_1_index] [atom_2_index] [calc_method] (naive, pygromos, numpy). Atom indices are 0-based. Default calc_method is pygromos."
    if (len(sys.argv) < 4 or len(sys.argv) > 5):
        print(usage)
        sys.exit(1)
    # process command line arguments and create the file object
    my_configuration = Cnf(sys.argv[1])
    atom_1 = int(sys.argv[2])
    atom_2 = int(sys.argv[3])
    if (len(sys.argv) == 4):
        method = "pygromos"
    else:
        method = sys.argv[4]
    # calculate the distance with the choosen method
    # get coordinates as numpy array
    coord = my_configuration.get_atom_coordinates()
    distance = 0.0
    if (method == "pygromos"):
        distance = distance_pygromos(atom_1 + 1, atom_2 + 1)
    elif (method == "naive"):
        distance = distance_naive(coord[atom_1], coord[atom_2])
    elif (method == "numpy"):
        distance = distance_numpy(coord[atom_1], coord[atom_2])
    else:
        print(usage)
        sys.exit(1)
    print(f"Selected method: {method}")
    print(distance)