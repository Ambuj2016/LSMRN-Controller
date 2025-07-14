# simulate_tracking.py
import numpy as np
import matplotlib.pyplot as plt
from lsmrn_controller import LSMRNController
from lnt_controller import LNTController

np.random.seed(42)

T = 200
ref_traj = np.sin(np.linspace(0, 4 * np.pi, T))

# LSMRN setup
lsmrn = LSMRNController()
x_robot = np.zeros(T)
uc_lsmrn = np.zeros(T)
e_lsmrn = np.zeros(T)

# LNT setup
lnt = LNTController()
x_lnt = np.zeros(T)
uc_lnt = np.zeros(T)
e_lnt = np.zeros(T)

for k in range(1, T):
    # LSMRN
    error = ref_traj[k-1] - x_robot[k-1]
    control = lsmrn.compute_control(np.array([x_robot[k-1], error, uc_lsmrn[k-1], ref_traj[k-1]]))
    x_robot[k] = 0.9 * x_robot[k-1] + 0.1 * control + 0.02 * np.random.randn()
    lsmrn.update_weights(error, uc_lsmrn[k-1], np.array([x_robot[k-1], error, uc_lsmrn[k-1], ref_traj[k-1]]))
    uc_lsmrn[k] = control
    e_lsmrn[k] = error

    # LNT
    error_lnt = ref_traj[k-1] - x_lnt[k-1]
    control_lnt = lnt.compute_control(error_lnt)
    x_lnt[k] = 0.9 * x_lnt[k-1] + 0.1 * control_lnt + 0.02 * np.random.randn()
    uc_lnt[k] = control_lnt
    e_lnt[k] = error_lnt

# Save results
np.savez("results.npz", ref=ref_traj, lsmrn=x_robot, lnt=x_lnt, e_lsmrn=e_lsmrn, e_lnt=e_lnt, uc_lsmrn=uc_lsmrn, uc_lnt=uc_lnt)
