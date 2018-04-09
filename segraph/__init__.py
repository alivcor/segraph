try:
    import numpy as np
except ImportError:
    print("NumPY is not installed. segraph needs NumPY to function. Please use 'pip install numpy' to install numpy.")
    exit(0)
from segraph import *
from segraph import create_graph