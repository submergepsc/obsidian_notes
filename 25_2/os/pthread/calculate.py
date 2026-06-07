import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 直接指定系统中存在的中文字体文件
font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
font_prop = fm.FontProperties(fname=font_path)
# 解决负号显示问题
plt.rcParams["axes.unicode_minus"] = False
df = pd.read_csv("results.csv")
avg = df.groupby("threads", as_index=False)["time_sec"].mean()
avg = avg.rename(columns={"time_sec": "avg_time_sec"})
t1 = avg.loc[avg["threads"] == 1, "avg_time_sec"].iloc[0]
avg["actual_speedup"] = t1 / avg["avg_time_sec"]
avg["ideal_speedup"] = avg["threads"]
plt.figure(figsize=(8, 5.5))
plt.plot(avg["threads"], avg["actual_speedup"], marker="o", label="实际加速比")
plt.plot(avg["threads"], avg["ideal_speedup"], marker="o", label="理想加速比")
plt.xlabel("线程数", fontproperties=font_prop)
plt.ylabel("加速比", fontproperties=font_prop)
plt.title("矩阵乘法加速比曲线", fontproperties=font_prop)
plt.xticks(avg["threads"])
plt.grid(True)
plt.legend(prop=font_prop)
# 让坐标刻度也使用中文字体
ax = plt.gca()
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font_prop)
plt.tight_layout()
plt.savefig("speedup_curve.png", dpi=200)
plt.show()