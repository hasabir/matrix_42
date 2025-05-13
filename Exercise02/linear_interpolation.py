import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from Exercise00.add_subtract_scale import Vector
from typing import TypeVar, Generic, List








def lerp(u: V, v: V, t: float) -> V:
    """
    Linear interpolation between two vectors u and v with a parameter t.
    """
    return u.scl(1 - t).add(v.scl(t))