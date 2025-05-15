import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))

from Exercise00.add_subtract_scale import Vector, Matrix

from typing import TypeVar, Generic, List
import numpy as np
f32 = np.float32