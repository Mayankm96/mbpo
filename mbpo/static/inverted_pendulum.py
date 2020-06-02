import sys
import numpy as np
import pdb

"""
Fo MuJoCo Inverted Pendulum
"""
# class StaticFns:
#
#     @staticmethod
#     def termination_fn(obs, act, next_obs):
#         assert len(obs.shape) == len(next_obs.shape) == len(act.shape) == 2
#
#         notdone = np.isfinite(next_obs).all(axis=-1) \
#         		  * (np.abs(next_obs[:,1]) <= .2)
#         done = ~notdone
#
#         done = done[:,None]
#
#         return done

"""
For SiMBL Inverted Pendulum
"""
class StaticFns:

    @staticmethod
    def termination_fn(obs, act, next_obs):
        assert len(obs.shape) == len(next_obs.shape) == len(act.shape) == 2

        state_high = np.array([1, 1])
        state_term = np.any(next_obs > state_high) or np.any(next_obs < -state_high)

        done = state_term

        return done