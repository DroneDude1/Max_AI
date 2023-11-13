"""
Test file for Max_Adam

Max Clemetsen
PY 3.10
10/16/23
"""

from tests import *
import MaxAdam as MA
from gan_test import *

if __name__ == "__main__":
    mnist_multiple_test(MA.MaxAdamCallback, MA.AdAlpha_Momentum, epochs=5, learning_rate=0.01, chaos_punishment=6)
