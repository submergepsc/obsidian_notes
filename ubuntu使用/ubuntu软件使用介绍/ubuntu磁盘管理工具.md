gdu > ncdu , 
df -h :整体分析
baobab,：ui界面直观 --对标wiztree
dust：树状结构，
dua, ： 迅速
	

**最后：**  gdu,  baobab，




**gparted** win+x对标：sudo gparted





你之前已经提到过一批挺主流的 Linux 磁盘/空间分析工具了，我帮你**系统梳理一版“分层+对比+使用场景”总结**，把你提到的 + 常见但你没问到的都补齐一下，避免你再踩坑。

---

# 🧭 一、核心分类（先建立全局认知）

磁盘工具其实可以分成 4 大类：

### 1️⃣ 空间占用分析（你现在最需要的）

👉 查“谁占空间”

* ncdu
* gdu
* dua
* baobab
* dust（补充）

---

### 2️⃣ 文件/目录统计工具（底层）

👉 查“多少 + 多大”

* du
* df

---

### 3️⃣ 磁盘管理 / 分区工具

👉 查“磁盘结构”

* fdisk
* lsblk
* parted
* gparted

---

### 4️⃣ 文件系统/清理工具

👉 查“垃圾 / 重复 / 无用”

* bleachbit
* fdupes
* rdfind
![](assets/Pasted%20image%2020260423145952.png)
---

# 🔍 二、你重点问的几个工具对比（核心）

## 🔹 1. ncdu（你已经用过）

![Image](https://images.openai.com/static-rsc-4/sNKBUqpTN9ezFPcvGc320Ac9u9IYyMcP2_09vLI_Y47kKP6AufwgHKHgYVDv8Gca1QoSwhQ2z_7Xu-filRenmoI4rw1ZaUP7StyKCGn-hPqehr8_lZDk0Z0b6Kj47rxq4uztnDYlJjgThiFb8Gc5zE_So-Hv0IsdafY-36xXb9T3Y82K3rKTeCoFw4mLgAqc?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/F-yNyby8LwKwKR53mDRy_R0I6sN7s-piEb5m7JdVDLsootg2LttoPfheEXNShplzch6-P2bmTxaCGKwC3Ztoz49F1KdGdIvZ001I1y6uw1IbOPeNtlLTTRZxAW_CNO4dMinmW8hvyy5nso-jYlQM4O8dfXWb5Yqzr9Sw7xyzsHuiUIBZIgei6ynPwPoXsCQF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/wVJW4CQEbbNYCRCtCRiFhD46NeNGO8vVH5M7dpQwpJBbpsMBE7bbuDBTNIOBKAb1oFzmJJ9aUljlXOJ6_hcaVLg5cjUF7igOQ5jAsI3a99OOUuS0Lt4ml1TGIdaisay8JjriRwF5cI1tKfg6J8stWmeVJKv9NgEo7-UhQkeQ0vdl47KR29_IIfeTJxmrdKoj?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Lb-7dAHFopdPlwl26Ezv6djnijFcYfYXnEb6WG_mppyCI51vnr3UzFAb9C70195a0oxfg3aIZlTz6lL2Dm7KOPrXjL8mqgc9fVmZgAHpQWsXh7FpgK9hil9QC8X-dIb98Lmgli43uARzqJ8QBz_TbNJJ0VUgPK8o1NDe8jJagqqMhNCZGB-scrI4LYofre3H?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/IQLcuySHjdtY5PdaOj8JtRkGHHdoOoDCz3VAUGuPpp-N8gY9VrloTM8CCwhMOq2sdXWHNjJambYiwdHeNlBkBEvpihuEC0Sc6mQpNKZS2SIQeeQ9rJui6EJALRhGx6o3L7ahCwXqmNPczHjyW8APqrIIpAwOHrhgZsOhnBzvjbPT7khiH_ViB95nYBUWt06l?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/gyqSfoI993iniygBeb_cIobrWYdovjQ9TgUjioYk_PiVZn3nCtmpYieSX-wd0cZ5qIZZi-8sB75W-oEQnAqznc5W7dCNaua7SoV6eLr8jSAoJQHOJ4HoRqEl4c1FoXwbddajDHFUXVduTxF3FOkuMNJxSJG2lkHixUNI1DolKTBtcjUhw8z7EhHGnfSjIazO?purpose=fullsize)

👉 名字：**NCurses Disk Usage**

✔ 特点：

* 终端 UI（可交互）
* 可以直接删除文件
* 快速（比 du 强很多）

✔ 适合：
👉 **最通用 / 推荐首选**

```bash
ncdu /
```

---

## 🔹 2. gdu（现代版 ncdu）

![Image](https://images.openai.com/static-rsc-4/2UGK4xeqfGizRJLGbOEMHQ8cSyMuxYT1tzwBeISfU1XbtVmLDXAGV7MX5WrfqP3ZgqBR53v7we7FhurbwSPCiq3ACj2gcrDOmEANX7Dbzk8l7KqH4HqJsy7lKs-5DnZIbUypUZ3v9Eq51odoPDYRXbjGQZYfoDbc7ddZHsmW8lPgZG88EgoUDhztUzHPwF8B?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/X3MMlsYA6Iumh4D8HRm91ETux63r9nBKdkAdJv1LEu5iEEd123zPeDKyGNE3OYzu9Cja-EfEFa_k3puVXEJAMj57gjZpKi6JG2tSaVNKsY1N-ROce2XDVsG97W4fBc291YskVtOWfLIQblKCi3hTgmaRvHlezOPYkgcekAbbNjmBV_lYBRWDS5kEbkI4lGWG?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/pKu4wQ8nFT-Agw_r2q2OLxSEs3MMBaojJl8ESl43SgkHR886K5SiX4t3oP0FWaXsoFQMnLk5TdhZomiydElXga1VSbVJcyIeGsnxXnIYQgDViO0xdkBz4FrH_f5NU3vsG1THY_NYTy-f7Y1HST-UgvukOnMoxeW9nAfkyIjSb6-RIfV2KJL4JLfqvdnmJNOz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/-S6xi2QuwASxzRf5VQK9KT1x1cD4Oq0ZeuOTKncS0dTyiAAE8v228y1xigeS9hJH1hvWSRblHL7Jr71M5-mNLG7XT9Wh50N-kCGN7h9c81Vyzae1KzBRpAGrMeCwX_IuKXxsqfd-LT7dYcjUYkvciheoqOcJgJgz-YcqiSGwBue1ALtly2w31gcE_SzAAzN6?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/B-Z7NsW25SG8ft-GDjM5T0rXYEWO11pkpnRwfhgqvDRYy0aaAj7Z4u5A6WPG989SWtKSv1Iv33S1RLbEi2gfJuBLJny050TjApPn0WEYczzqAcXH3oYe4IFpuMD0pYuVStAV6tFu30Dp1zJUnGyIfRxoiQWNm3G_QrAUHU_M97mZcjfT31f8S6rkfFgTyB28?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/YZcsvyBGpftJR-nZtdTULS6stsl8y4fy_PqovfbvVieN53jhQisQy-asNsERU1XwuWBrEJJrHRkGVpi4HyOG-yXjwzWAJWMCJsOJnTgopb9XnEfL95Rpkd5ExTlDGngFQ-kPayRWLqbSLgH0c1b6-J-NhiOX_vvtLzvBNZKYjOqytrmmh3u5ASUgQNmFghck?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/84Qux20TokANKC4QbhK3jL5OuldGn9wLUZf78jpU3uyFQDOLC8QInMQ25WuD5gW-JFWeON3ovTCC_RnaV13I-ZZlUbDyuKTelfN9GRMbA28WF-lDrL179NBguZ_hQTOY3UWjWaZ0k-NZGFs4ge0ZQjNnOuZHJWbXUlYHD2Y0t4AOrbHom3DWz_AVN9KpfihI?purpose=fullsize)

👉 名字：**Go Disk Usage**

✔ 特点：

* 用 Go 写的
* 极快（SSD 上很明显）
* UI 和 ncdu 很像

✔ 适合：
👉 **大磁盘 / 文件特别多时更爽**

---

## 🔹 3. dua（可视化更强）

![Image](https://images.openai.com/static-rsc-4/23LEprYj66zWGjsgUQHD4jhRRFqJsCm2y0m_YltZV7F68XWJirvfhqsK5RPiuCuaKft-X2xqioK9SP4YljFPVKRuXCrZHuIaSPdBly2XeEsuGTPqX5rxbUXEZ9u7kj7YuwY4_IQWtERTsG2Cip-0rWa3PBYojIHNNznRcB5URizjXoBvozMJ0rE21QaGxDDW?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/N8PO47vaIcQ3jF2kP0NPJOxCmWsgZRKL_FIEAx0VsKkEwnlcz-zEBMZtwb1Uq-ckyH25PZ7Jc2UAgvjB52XPFGInzwZJl486iHQQ4usDhD6Be0Y3EpKFJ3ztVHp28h1BOcjV2F4TQcmCu997BjzXJA7uklMRSXa4g_xilQDM5MWCU8rkIT5UffUvXlT2wJNw?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/nHmr9iXkK8nikzj5z6hrlsFUl4PqKlJVIZjBNwJif2SxqsBRka93WNtFRVk-s82rSPvc5SHkKNFHKhspx0OJRseZd_WOkwHjExsgWeKUaOrVlRRD0h5hDXCyGzufVGAEWbP3fBu9yrWR65dsxENNfa6SQhnZazg-Yi5_2F5rN9moazMdQ4A0IdjU0lHMiC8S?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/YSiqsvfRfzNYykiErZPyWpcBE8KtGgF80aPZTkdKfwecWljb-JFWL8iGk9OG4inpgkMIvKidwVY5O2PZ4jQhuOzj_9zGf-KSYEbGYpJC-iCxyBW_258Udb9udylj4Ptj36R56Qd8ZngB8s7wuZrXzTjEiwg2YCxmBWmcOkuI_8vmlRbfJFKliB651vBfxQkp?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/XhTL15yTjcIOxegbWI0VwTmog2mIA-BGEUvDRq1MOW--hXF6qemZEaR4RbeVzwWkNx_YpCUgjdsSqf6Qi8WE1rG7CJD89WC9RzI8y4bpWpWTX9exr862ZkcpxGyeKa9Ze6BC9d6MOMoPJRf_zKScHUYUfnVFdn8NLrC446ondTLrSBav0UgGk2EVIFUpj_vW?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TUPvkY0Jv9enfzwJ6f9Mc6UGW83ZxotiIzwUgb8vWbm9B13ctCI1YpBgIXWsknkvdMj16jx6PkJhiK2tWzI_H2OaZF9vjHlkhyW_BrF_r_ylCobuUez7rb3gyXLa2IACAaeEj70GIXKy3m4XZ_FfigmvB13JOeGoK7WB9HYGQkZwi-Oj5M71itv135DrMAUZ?purpose=fullsize)

👉 名字：**Disk Usage Analyzer**

✔ 特点：

* 更现代 UI
* 支持交互筛选
* 支持导出 JSON

✔ 适合：
👉 **想分析结构/做数据处理**

---

## 🔹 4. baobab（GUI）

![Image](https://images.openai.com/static-rsc-4/ZKmt_CT61X4oobWTvIx9WG1T_5mJtJWrQnPrhiqkzUEavSXUQffcItrF1RIEBVUiNIH4zviRjWg1x8blyOnWpq90ocH0-OdJckTXy0nGWlae4K4vu4i-ijxiOyFTBbGW7AJk3wKyk7HIB_zchT6Q3drNn_E141v6WIRQQs5weruKbuV8-WIjkl45W2NkvRcA?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/jm_ukPK3KCJWIBYMkgi4mX1jtaNauMetEmSfSpebcK9IKv33SVleouuV7t8i4e63bbJVBF1v5hPIFxhsicMFL-V0cgQB_pBjz4nnoUs39ixDYCbiTCYN_t47crdoD2osaym48WSO4l8q1T34FeF_AsJM5f1K_kelEJUYpZpIAhaD1ltsxm6LW-5o0CGQ5qta?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/AA8QyTSkUKVwULXW3bHohgRUntNTicfxYkJjyAforbSQ6FrBBeLX95hY3sIbB5sbZ_ythwoHljKMUTI8BDJusM6uudoTb4fiZ_jG_qgA9OQsLlCEdD4AAz7VordNsFzhOCd7ca0IFg8z0nbkP1kySmK0d9hhYCapqNSV30ped3p-7lp09nzAX35WbRaNgLSr?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ht3VKroWt7KUSmuMm7uqXW_gPtr-g9YMmoXjh0ml4M4snHzNKPiS92eaqQUN9YCuLDadT1LN8dU7dqDtgZ6-9nkrNol84YpAc6OXNQ-51pscM8L7za8mZDi6r2p3Ct7Mh1BhOuQ6HtTjsk63ojD3wZBCRmz6BjgNsV82exQ07U3JXvBwNz6oiIRcc07P8Cy1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tQg9cMLFrnoOtB08aMqOtffmIndPenajEQwNRrDHUrN6DlKq31mJR1Qv-uKGi86gb1_YqhQxkcKHZI0yn5Vp-AFPD7KmV5doCiBnCuZUSrxW9yHziqcPLQsqbNsQHlyvLLUo-86oKc_tya7kaX4zEPC31eBKyUaESXz_v7CA47R9jIBGD83VkGA5u5hOjJxt?purpose=fullsize)

👉 全名：**GNOME Disk Usage Analyzer**

✔ 特点：

* 图形界面（圆形图）
* 一眼看结构

✔ 适合：
👉 **新手 / 想直观看**

---

## 🔹 5. dust（你没提但很好用）

![Image](https://images.openai.com/static-rsc-4/yk05vQcrHjsvOpOBuBVzf8EZrx3R_VDntPGhUgV2jt_rFLqNKJYebNDQNx9DJ9qHOoT-UZaFr9lb4TTgtGRmTVKNCPvGEPUSinMZwZ7Us3bvzoCbIQ9YPE8Ih-PLU7B51wZ9M_PEReXDdojYosBwY4X93IgloY5URSyekZCQsz2468Ximyw7eln4Fyxw58tU?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/O4KQzk9E_M7Dz1O4BzfSopzas20jsD7bJO-etSL4zz5V2X3_VlNjVMuShT1HKgnN9YHMThT8QEzrP5uM22W6vgai6-Y5R-mPpuTqW8pQJ8LLbmGzHmbCLQ6nnaXbgS3dkbDoUtC4ooHTO6tebiE5LHS_AcM6woo4O1UxHcncvBURLbgMovRBlNjHlw-mwNeN?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/BikwIWKLJhG4LXtrOAWbEZM6z6ZTyfwCKIcEMS-wIwhiR9mCpYgVL91o0hRbLNP5iAPGyHhGomEePPb09Yjr6lXI34LNOVBT7LAhtQ0txxgw-G8qomFxMJPfhPMUQxY23_jvqU3-owv-KU3-PeI4jzfgBvLmPpJNiJ0-NbTWZZjKRmO0liEjfHcf5coqUFcU?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/7JuYg6iVADn8oOLYEhORyrwTybYu3CODcjmAZFzfC1swRR5ycOjcYgqr6XYBDdhk5Bin1eoyRBG5HpyvqD2OBWHgNoWoCQKgZOVyP--IefbDl7qX1tHKwu-fXN3mzm_k69BqByR4fCsdVe1N8_JdBHOffu-mwAPscR3tzKUzpsTwUn0TCp0gfdmy7QcV9dRO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/uyY6rjZlphdpUKoPgBFuN3WkY3tGdGOeoFCEe--msQgxPqiXtE6SjtlpcovyvCJSm__tFyI9h7vMr01-jAgwZU-MQeJNDBbbBb3rT-ieLBLnuKb3ZGalIWOv37LiJ-HkjpyheQdW9L1ONp5zxpDRKtMHyHa7kNPaXbJ-gsLNp03tgJ2wQYLVdrMBQLZqsmMo?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/8tgp8iekW-Ijit2fzuAh4rqmmZ0r037JxYgypy_GpRFaoMD3HaGrGoGPJoLehyRIvUvkC6FXWoXMRUiZcyjgA9_iuKSpwO4lJEoPR5oHsbGWPe69qLV93lxZUSG5OXJzXCP8UospleMr-bSLYlpn1gYsAVxr8ModnsLpReQEV9tIRacpwF7OQvGHR6dSb1ir?purpose=fullsize)

👉 Rust 写的

✔ 特点：

* 彩色树状图
* 非常直观
* 比 du 好太多

```bash
dust
```

👉 适合：**快速扫一眼**

---

# ⚙️ 三、底层工具（你提到 du 不够用）

## 🔹 du（你说“不够用”的那个）

```bash
du -h --max-depth=1
```

❌ 问题：

* 慢
* 不可交互
* 不直观

✔ 本质：
👉 所有工具的“底层”

---

## 🔹 df（查磁盘总量）

```bash
df -h
```

👉 用来回答：

* 磁盘满了吗？
* 哪个分区满？

---

# 💣 四、为什么你会觉得不够用（本质原因）

你现在的场景是：

👉 仓库 + 图片 + TeX + .git 爆炸

这种情况：

| 工具     | 是否适合  |
| ------ | ----- |
| du     | ❌     |
| ncdu   | ✅     |
| gdu    | ✅（更快） |
| baobab | ✅（直观） |

---

# 🧨 五、你刚才提到的典型“占空间怪物”

你截图里那些：

### 1️⃣ TeX Live

👉 基本全是字体 + 宏包
👉 几 GB 很正常

---

### 2️⃣ `.git`

👉 **版本历史 + 图片重复存储**

👉 关键点：

* Git 每次改图片 = 新副本
* 不会“只存一份”

---

### 3️⃣ node_modules

👉 小文件地狱（几十万文件）

---

# 🧠 六、推荐你的最优组合（实用）

直接给你结论：

### 🚀 日常查空间

```bash
gdu /
```

或

```bash
ncdu /
```

---

### 🔍 快速扫一眼

```bash
dust
```

---

### 🖥 图形分析

```bash
baobab
```

---

### 🧹 查重复文件

```bash
fdupes -r .
```

---

# 🧾 七、一句话总结

👉 你可以这样理解：

* `du` = 原始 API
* `ncdu / gdu` = 现代 CLI
* `baobab` = GUI
* `dust` = 快速浏览

---

# ⚠️ 最关键建议（结合你之前的问题）

你现在的问题核心不是工具，而是：

👉 **Git + 图片 = 爆炸增长**

如果你继续这样用：

* 仓库会越来越离谱
* 再多工具也救不了

---

如果你愿意，我可以下一步帮你做这个👇：

👉 **“1000 张图片仓库 → 图床 + 自动迁移方案（一次性解决）”**

这个才是真正解决你问题的关键。
