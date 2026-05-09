import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mutex_results.csv")

avg = df.groupby("N")["time"].mean().reset_index()

plt.figure()
plt.plot(avg["N"], avg["time"], marker="o")
plt.xlabel("N")
plt.ylabel("Time (s)")
plt.title("Mutex Counter: N-Time Curve")
plt.grid(True)
plt.savefig("mutex_curve.png", dpi=300)
plt.show()
