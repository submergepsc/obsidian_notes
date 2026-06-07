import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 直接指定字体文件，避免找不到字体名
font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["axes.unicode_minus"] = False
# 读取数据
df = pd.read_csv("results.csv")
# 计算每个线程数的平均运行时间
avg = df.groupby("threads")["time_sec"].mean().reset_index()
# 计算加速比
t1 = avg.loc[avg["threads"] == 1, "time_sec"].values[0]
avg["speedup"] = t1 / avg["time_sec"]
# 理想加速比
avg["ideal"] = avg["threads"]
# 画图
plt.figure(figsize=(8, 5))
plt.plot(avg["threads"], avg["speedup"], marker="o", label="实际加速比")
plt.plot(avg["threads"], avg["ideal"], linestyle="--", label="理想加速比")
plt.xlabel("线程数", fontproperties=font_prop)
plt.ylabel("加速比", fontproperties=font_prop)
plt.title("Go矩阵乘法加速比对比图", fontproperties=font_prop)
legend = plt.legend(prop=font_prop)
plt.grid(True)
# 让刻度标签也用中文字体
ax = plt.gca()
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font_prop)
plt.tight_layout()
plt.savefig("加速比.png", dpi=300)
print("\n各线程平均运行时间：")
print(avg[["threads", "time_sec"]])