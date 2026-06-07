import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 指定中文字体（你已经有这个路径）
font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["axes.unicode_minus"] = False
# 读取数据（带容错）
df = pd.read_csv("results_prime.csv", on_bad_lines="skip")
# 转换数据类型
df["threads"] = pd.to_numeric(df["threads"], errors="coerce")
df["run"] = pd.to_numeric(df["run"], errors="coerce")
df["time_sec"] = pd.to_numeric(df["time_sec"], errors="coerce")
df = df.dropna()
df["threads"] = df["threads"].astype(int)
df["run"] = df["run"].astype(int)
df["time_sec"] = df["time_sec"].astype(float)
# 计算平均时间
avg = df.groupby("threads", as_index=False)["time_sec"].mean()
avg = avg.rename(columns={"time_sec": "avg_time_sec"})
# 计算加速比
t1 = avg.loc[avg["threads"] == 1, "avg_time_sec"].iloc[0]
avg["actual_speedup"] = t1 / avg["avg_time_sec"]
avg["ideal_speedup"] = avg["threads"]
print(avg)
# 画图
plt.figure(figsize=(8, 5.5))
plt.plot(avg["threads"], avg["actual_speedup"],
         marker="o", label="实际加速比")
plt.plot(avg["threads"], avg["ideal_speedup"],
         marker="o", label="理想加速比")
# 中文标签（关键：加 fontproperties）
plt.xlabel("线程数", fontproperties=font_prop)
plt.ylabel("加速比", fontproperties=font_prop)
plt.title("质数筛选加速比曲线", fontproperties=font_prop)
plt.xticks(avg["threads"])
plt.grid(True)
plt.legend(prop=font_prop)
plt.tight_layout()
plt.savefig("prime_speedup_curve.png", dpi=200)
# 如果你在服务器环境，这行可以删掉
# plt.show()