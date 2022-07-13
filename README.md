# distance-calculator
Calculates distances between two atoms in a GROMOS cnf file

`distance.py` contains functions to calculate the geometric distance between two atoms and can also be used as standalone.

`example_usage.py` uses some of these functions in another script.

Tests make sure that distances are actually computed correctly, especially when switching from 0-based to 1-based arrays.
