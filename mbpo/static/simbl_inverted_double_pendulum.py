import sys
import numpy as np
import pdb

"""
For SiMBL Double Pendulum
"""


class StaticFns:

    @staticmethod
    def termination_fn(obs, act, next_obs):
        # Always false (true for environment version v1)
        done = np.zeros((obs.shape[0], 1), dtype=bool)
        return done
