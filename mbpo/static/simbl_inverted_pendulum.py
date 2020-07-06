import sys
import numpy as np
import pdb

"""
For SiMBL Inverted Pendulum
"""


class StaticFns:

    @staticmethod
    def termination_fn(obs, act, next_obs):
        # assert len(obs.shape) == len(next_obs.shape) == len(act.shape) == 2
        #
        # state_high = np.array([1, 1])
        # state_term_high = np.any(next_obs > state_high, axis=1)
        # state_term_low = np.any(next_obs < -state_high, axis=1)
        #
        # done = np.any(np.stack([state_term_high, state_term_low], axis=1), axis=1)
        # print(done.shape)
        # # make it batched
        # done = done[:, None]
        #
        # return done

        # Always false (true for environment version v2)
        done = np.zeros((obs.shape[0], 1), dtype=bool)
        return done
