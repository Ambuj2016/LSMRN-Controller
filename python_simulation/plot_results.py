# plot_results.py
import numpy as np
import matplotlib.pyplot as plt

data = np.load("results.npz")
ref = data["ref"]
lsmrn = data["lsmrn"]
lnt = data["lnt"]
e_lsmrn = data["e_lsmrn"]
e_lnt = data["e_lnt"]
uc_lsmrn = data["uc_lsmrn"]
uc_lnt = data["uc_lnt"]

plt.figure(figsize=(10, 6))
plt.plot(ref, label="Reference", linestyle="--")
plt.plot(lsmrn, label="LSMRN Output", linewidth=2)
plt.plot(lnt, label="LNT Output", linewidth=2)
plt.title("Trajectory Tracking")
plt.xlabel("Time Steps")
plt.ylabel("Output")
plt.legend()
plt.grid(True)
plt.savefig("trajectory_tracking.png", dpi=300)

plt.figure(figsize=(10, 5))
plt.plot(e_lsmrn, label="LSMRN Error")
plt.plot(e_lnt, label="LNT Error")
plt.title("Tracking Error")
plt.xlabel("Time")
plt.ylabel("RMSE")
plt.legend()
plt.grid(True)
plt.savefig("tracking_error.png", dpi=300)

plt.figure(figsize=(10, 5))
plt.plot(uc_lsmrn, label="LSMRN Control")
plt.plot(uc_lnt, label="LNT Control")
plt.title("Control Effort Comparison")
plt.xlabel("Time")
plt.ylabel("Control Signal")
plt.legend()
plt.grid(True)
plt.savefig("control_effort.png", dpi=300)

plt.show()
