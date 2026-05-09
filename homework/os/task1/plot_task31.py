import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("task31_results.csv")

df["time_sec"] = pd.to_numeric(df["time_sec"], errors="coerce")
df = df.dropna(subset=["time_sec"])

avg = df.groupby(["program", "threads"], as_index=False)["time_sec"].mean()

print(avg)

plt.figure(figsize=(8, 5))

order = [
    "counter_mutex",
    "counter_atomic_relaxed",
    "counter_atomic_seqcst",
    "counter_spin",
]

for program in order:
    sub = avg[avg["program"] == program]
    if not sub.empty:
        plt.plot(sub["threads"], sub["time_sec"], marker="o", label=program)

plt.xlabel("Number of threads N")
plt.ylabel("Average time / seconds")
plt.title("Performance comparison of mutex, atomic and spinlock")
plt.xticks([1, 2, 4, 8, 16])
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("task31_performance.png", dpi=300)
plt.show()

