# gdist
Calculates distances between two atoms in a Gromos cnf file (gdist = Gromos distances)

`distance.py` contains functions to calculate the geometric distance between two atoms and can also be used as standalone.

`example_usage.py` uses some of these functions in another script.

Tests make sure that distances are actually computed correctly, especially when switching from 0-based to 1-based arrays.

# Installation

Make sure to have `PyGromosTools` installed (https://github.com/rinikerlab/PyGromosTools). Then run `python -m pip -e .` in the root directory of this repo. To execute tests, run `make test`.
