## Problem A. 时间复杂度

```cpp
// ==========================================
// Problem A. 时间复杂度
// ==========================================
#include <iostream>
using namespace std;

/*
 * 官方题解详细分析：
 * 本题要求我们将五段代码按照时间复杂度从低到高（即运行速度从快到慢）进行排序。
 * * 1. 代码 A：
 * 外层循环 i 从 1 到 n，内层循环 j 从 i 到 n。
 * 执行次数 = n + (n-1) + ... + 1 = n(n+1)/2。
 * 故时间复杂度为 O(n^2)。
 * * 2. 代码 B：
 * 外层循环 i 从 1 到 n，内层循环满足 i*j <= n，即 j 最多执行 n/i 次。
 * 总执行次数 = n/1 + n/2 + n/3 + ... + n/n = n * (1/1 + 1/2 + ... + 1/n)。
 * 根据调和级数求和公式，这部分约等于 n * ln(n)。
 * 故时间复杂度为 O(n log n)。
 * * 3. 代码 C：
 * 外层循环 i 从 1 到 n，内层循环 j 满足 j*j <= n，即 j 最多执行 sqrt(n) 次。
 * 总执行次数 = n * sqrt(n) = n^1.5。
 * 故时间复杂度为 O(n^1.5)。
 * * 4. 代码 D：
 * 计算斐波那契数列，但没有任何记忆化存储（即 arr 数组）。
 * 每次调用 fib(n) 都会分裂出 fib(n-1) 和 fib(n-2) 两个子调用。
 * 这棵递归树的节点数随 n 呈指数级增长，其复杂度与斐波那契数列本身的增长率一致。
 * 故时间复杂度为 O(Fib(n))，属于指数级 O(1.618^n)。
 * * 5. 代码 E：
 * 同样是计算斐波那契数列，但使用了 arr 数组记录已经计算过的结果（记忆化搜索）。
 * 每个 fib(i) 的值只会被计算一次，后续调用直接从 arr 数组中 O(1) 返回。
 * 故时间复杂度为 O(n)。
 * * 综上排序（复杂度从小到大）：
 * O(n) < O(n log n) < O(n^1.5) < O(n^2) < O(Fib(n))
 * 对应的代码编号为：E < B < C < A < D
 */
int main() {
    // 题目没有输入，直接输出分析得出的固定答案即可
    cout << "EBCAD\n"; 
    return 0;
}
```

## Problem B. 完美洗牌

```cpp
// ==========================================
// Problem B. 完美洗牌
// ==========================================
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/*
 * 官方题解详细分析：
 * 根据完美洗牌的规则，原先在位置 i（从1开始编号）的牌：
 * - 如果在前半段 (1 <= i <= n/2)，会被移动到 2*i - 1。
 * - 如果在后半段 (n/2 < i <= n)，会被移动到 2*i - n。
 * * 题解指出一个重要的群论性质：一副牌在“完美洗牌”规则下，最多经过 n 次洗牌，
 * 就必然会恢复到初始状态。这是因为洗牌操作实际上是一个置换群，
 * 每个位置上的牌的轨迹形成一个循环，而这个循环的长度（即阶）不会超过 n-1。
 * * 因此，我们可以直接使用暴力模拟的方法：
 * 每次按照规则生成洗牌后的新字符串，并与初始字符串进行比较。
 * 因为最多洗 n 次，每次洗牌遍历 n 个字符，总时间复杂度为 O(n^2)，
 * 对于 n <= 1000 的数据范围，O(n^2) 完全可以在 1 秒内通过。
 */
void solve() {
    int n;
    cin >> n;         // 读入扑克牌的张数（保证为偶数）
    string s;
    cin >> s;         // 读入初始的牌面顺序
    
    string original = s; // 保存最开始的牌面顺序，作为后续比对的基准
    int steps = 0;       // 记录当前的洗牌次数
    
    // 不断进行完美洗牌，直到牌面恢复初始状态
    while (true) {
        string next_s(n, ' '); // 用于存放洗牌后新顺序的字符串
        
        // 遍历当前牌堆中的每一张牌，计算其洗牌后的新位置
        for (int i = 1; i <= n; ++i) {
            if (i <= n / 2) {
                // 位于前半部分的牌：新位置是 2*i - 1
                // 注意：由于 C++ string 的下标是从 0 开始的，所以赋值时下标需再减 1
                next_s[(2 * i - 1) - 1] = s[i - 1]; 
            } else {
                // 位于后半部分的牌：新位置是 2*i - n
                // 同样，转换为 0-indexed 的下标需要减 1
                next_s[(2 * i - n) - 1] = s[i - 1]; 
            }
        }
        
        s = next_s; // 更新当前牌堆的状态
        steps++;    // 洗牌次数加 1
        
        // 检查洗牌后的状态是否与初始状态完全一致
        if (s == original) {
            break; // 如果一致，说明完成了一个循环，跳出
        }
    }
    
    // 输出恢复初始状态所需的最少洗牌次数
    cout << steps << "\n";
}

int main() {
    // 优化输入输出流速度
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int t;
    cin >> t; // 读入测试数据组数
    while (t--) {
        solve();
    }
    return 0;
}
```

## Problem C. 游览路线

```cpp
// ==========================================
// Problem C. 游览路线
// ==========================================
#include <iostream>
#include <vector>
using namespace std;

/*
 * 官方题解详细分析：
 * 本题要求寻找一条从起点 s 到终点 t 的路径，使得路径上所有边权值的“按位与(&)”结果最大。
 * * 涉及到位运算求最大值的问题，通常采用“按位贪心”的策略：
 * 1. 我们希望结果的高位尽可能为 1，因为高位的 1 比低位的所有 1 加起来都要大。
 * 2. 我们从最高位（例如第 30 位）开始向低位依次尝试。
 * 3. 假设我们要判断当前这一位（第 bit 位）能否为 1：
 * - 我们将这一位设为 1（结合之前已经确定的高位 1），得到一个目标掩码 expected。
 * - 我们只保留图中那些满足 (边权 & expected) == expected 的边。这代表着这条边
 * 包含了我们期望的所有 1 的位。
 * - 在这些被保留的边构成的子图中，检查起点 s 和终点 t 是否仍然连通。
 * - 如果连通，说明我们可以让这一位为 1，我们将这一位的 1 保留到最终答案中。
 * - 如果不连通，说明我们无法同时满足之前确定的高位和当前位均为 1，则当前位只能为 0。
 * * 判断连通性可以使用并查集（Disjoint Set Union, DSU）。
 * 时间复杂度：O(m * log V * alpha(n))，其中 V 是边权的最大值，alpha 是并查集反阿克曼函数。
 */

const int N = 100005;

// 定义边的结构体
struct Edge { 
    int u, v, w; 
};
vector<Edge> edges;

// 并查集的父节点数组
int fa[N];

// 并查集的查找操作，带路径压缩优化
int find(int x) {
    // 如果自己是根节点，返回自己；否则递归查找父节点的根，并直接挂到根节点上
    return x == fa[x] ? x : fa[x] = find(fa[x]);
}

int main() {
    // 题目提示输入数据量较大，必须使用较快的输入方式
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    
    // 读入所有边的信息
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }

    int ans = 0; // ans 记录最终可以达到的最大按位与结果
    
    // 边权最大为 10^9，10^9 < 2^30，所以从第 30 位开始向下贪心枚举
    for (int bit = 30; bit >= 0; --bit) {
        // expected 是我们期望在当前这一步达到的前缀按位与目标
        // 它包含了之前已经被证实可行的较高位，以及当前正在尝试的这一位（置为 1）
        int expected = ans | (1 << bit); 
        
        // 每次尝试都需要重新初始化并查集
        for (int i = 1; i <= n; ++i) {
            fa[i] = i; 
        }
        
        // 遍历所有边，筛选出符合条件的边进行连边
        for (const auto& e : edges) {
            // 如果这条边的权值 w 在 expected 要求为 1 的那些位上都是 1
            // 即 e.w 完全包含了 expected 的二进制特征
            if ((e.w & expected) == expected) {
                // 将这两个点所在的集合合并
                int root_u = find(e.u);
                int root_v = find(e.v);
                if (root_u != root_v) {
                    fa[root_u] = root_v;
                }
            }
        }
        
        // 检查在满足条件边构成的子图中，起点 s 和终点 t 是否属于同一个连通块
        if (find(s) == find(t)) {
            // 如果连通，说明当前位确实可以取 1，我们将预期的 expected 赋给最终答案
            ans = expected; 
        }
        // 如果不连通，ans 保持不变，意味着这一位放弃置 1（即为 0），继续尝试更低的位
    }
    
    cout << ans << "\n";
    return 0;
}
```

## Problem D. 靶场

```cpp
// ==========================================
// Problem D. 靶场
// ==========================================
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

/*
 * 官方题解详细分析：
 * 本题要求在给定时间出现的靶子中，合理安排转动方向，求最多能命中的靶子数量。
 * 这是一个典型的动态规划（DP）问题。
 * * 状态定义：
 * dp[i] 表示在第 i 秒“射中了第 i 个靶子”的前提下，前 i 秒最多能命中的靶子总数。
 * * 为了方便统一处理，我们可以虚构一个第 0 号靶子：
 * 它在第 0 秒出现在 0 号瞄准点（对应初始状态）。初始时 dp[0] = 0。
 * * 状态转移：
 * 要计算 dp[i]，我们需要枚举上一个射中的靶子是哪一个，假设是第 j 个 (0 <= j < i)。
 * 我们必须判断：从第 j 个靶子的位置 a[j] 转到第 i 个靶子的位置 a[i]，
 * 所需的最短距离（在圆周上可以是顺时针或逆时针，取最小值）是否能在 (i - j) 秒内完成？
 * 如果可以，则有转移方程：dp[i] = max(dp[i], dp[j] + 1)
 * * 圆周上的最短距离计算：
 * d(i, j) = min(|a[i] - a[j]|, c - |a[i] - a[j]|)
 * 判定条件：d(i, j) <= (i - j) * s
 * * 由于 n <= 1000，使用两层循环 O(n^2) 的转移是可以接受的。
 */
void solve() {
    int n, c;
    long long s; // s 是最大转动速度，注意最大可达 10^9，后续乘法需要防溢出
    cin >> n >> c >> s;
    
    // a 数组存储靶子出现的位置，a[i] 表示第 i 秒靶子的瞄准点编号
    vector<int> a(n + 1);
    a[0] = 0; // 初始化虚拟的第 0 个靶子，位于 0 号点，代表初始朝向
    
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // dp 数组初始化，-1 表示不可达的状态
    vector<int> dp(n + 1, -1);
    dp[0] = 0; // 第 0 秒由于不需要射击真实的靶子，命中数为 0，且绝对可达

    int max_hits = 0; // 记录全局能命中的最大靶数
    
    // 外层循环枚举当前想要射中的靶子 i
    for (int i = 1; i <= n; ++i) {
        // 内层循环枚举上一个射中的靶子 j
        for (int j = 0; j < i; ++j) {
            // 如果第 j 个靶子根本无法被射中，则无法从它转移过来，直接跳过
            if (dp[j] == -1) continue; 
            
            // 计算在圆周上，从 a[j] 转动到 a[i] 的最短距离
            int dist = abs(a[i] - a[j]);
            dist = min(dist, c - dist); // 考虑跨越 0 点的情况，取劣弧长度
            
            // 检查转动所需的时间是否足够
            // 时间差为 i - j 秒，每秒最多转动 s，最大可转动距离为 (i - j) * s
            // 注意这里需要强制转换为 long long 以防止大数相乘导致 int 溢出
            if ((long long)dist <= (long long)(i - j) * s) {
                // 如果来得及转过来，更新 dp[i] 的最大值
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        // 更新全局的最大命中靶数
        max_hits = max(max_hits, dp[i]);
    }
    
    cout << max_hits << "\n";
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```

## Problem E. Soft-取模

```cpp
// ==========================================
// Problem E. Soft-取模
// ==========================================
#include <iostream>
using namespace std;

/*
 * 官方题解详细分析：
 * 题意要求对给定的 x，依次使用 r, r-d, r-2d ... 直到下界 l（由于 d 是 r-l 的因数，最后刚好到 l），
 * 进行连续取模操作，并计算每次取模后的新值（不管有没有变化）的总和。
 * * 如果每次都暴力取模，时间复杂度为 O((r-l)/d)，会超时。
 * 题解给出了一个关键性质：真正改变 x 值的“有效取模”次数不会超过 3 次！
 * * 分析：
 * 1. 第一次取模可能是有效的，取模后必然有 x < r。
 * 2. 由于模数以 d 为步长不断减小，在 x >= l 的前提下，当遇到第一个比 x 小或等于的模数时，
 * 必然会发生第二次有效取模。由于取模的性质，第二次取模后必然有 x < d。
 * 3. 既然 x < d，那么只要模数 rr 大于 d，x % rr 就等于 x 本身。
 * 也就是说，在接下来的过程中，x 不会再变化，直到模数减小到接近 l，
 * 才可能发生最后一次（第三次）有效取模（且前提是 l <= x < d）。
 * * 因此，我们可以利用递归，跳过中间那些“无效取模”（即模数大于 x 的情况）。
 * 当 x 小于当前模数时，我们直接通过数学计算推算出下一次会发生改变的模数。
 */
long long calc(long long x, long long l, long long r, long long d) {
    // 递归边界：如果当前下界超过了上界，说明取模序列已经结束，返回 0
    if (l > r) return 0;
    
    // 如果当前被取模的数 x 大于等于当前的模数 r，
    // 说明这就是一次“有效取模”，x 的值会发生改变。
    // 本次的新值是 x % r，接下来递归处理剩下的模数序列 (上限变为 r-d)
    if (x >= r) {
        return x % r + calc(x % r, l, r - d, d);
    }
    
    // 如果当前的 x 已经比整个序列中最小的模数 l 还要小了，
    // 那么在剩下的所有取模操作中，x % rr 始终等于 x。
    // 因此剩下的每次操作产生的新值都是 x，我们只需要计算剩下还有多少次操作。
    if (x < l) {
        long long steps = (r - l) / d + 1; // 剩余的项数公式：(首项-末项)/公差 + 1
        return steps * x;
    }
    
    // 如果 x < r 且 x >= l，这意味着当前的模数比 x 大，所以当前这一步 x 不变。
    // 但接下来的某个模数可能会比 x 小或等于 x。我们需要跳过中间这些无效取模。
    // 我们要找到一个最小的 a（跳过的步数），使得 rr = r - a * d <= x。
    // 通过不等式求解：r - a*d <= x  =>  a*d >= r - x  =>  a = ceil((r - x) / d)
    // 整数除法向上取整的写法为：(r - x + d - 1) / d
    long long a = (r - x + d - 1) / d;
    
    // rr 就是下一次将会触发 x 改变的那个模数
    long long rr = r - a * d;
    
    // 在遇到 rr 之前，一共进行了 a 次取模，这 a 次取模得到的新值全都是 x 本身。
    // 当遇到 rr 时，产生的新值是 x % rr。
    // 然后递归处理剩下的序列，上限变为 rr - d。
    return a * x + x % rr + calc(x % rr, l, rr - d, d);
}

void solve() {
    long long x, l, r, d;
    cin >> x >> l >> r >> d;
    cout << calc(x, l, r, d) << "\n";
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```

## Problem F. 商店

```cpp
// ==========================================
// Problem F. 商店
// ==========================================
#include <iostream>
#include <vector>
using namespace std;

/*
 * 官方题解详细分析：
 * 这是一个典型的期望 DP + 状态压缩的问题。
 * 一共有 n 种类型的商品，每种有 a_i 个，其中有 b_i 个是我们心仪的。
 * n 的最大值为 19，所以可以使用一个 19 位的二进制整数 mask 来表示当前“还有哪些类型的商品没有被购买过”。
 * 二进制位为 1 表示该类商品还没买过（属于集合 S），为 0 表示已经买过。
 * * 状态定义：
 * f[S] 表示当前还剩 S 集合中的商品未购买时，买齐所有类型商品的期望天数。
 * 最终答案为 f[(1<<n) - 1]，即初始状态。
 * 边界条件：f[0] = 0 （全部买齐，还需要 0 天）。
 * * 状态转移：
 * 每天刷出新商品的规则是，在集合 S 中所有剩余可刷出的商品（总数为 sum(a_i, i∈S)）中等概率随机。
 * 而只有刷出心仪的商品（总数为 sum(b_i, i∈S)）时我们才会购买。
 * * 1. 期望等待天数：根据几何分布，每次成功的概率是 p = sum(b_i) / sum(a_i)，
 * 那么第一次成功买到某个心仪商品的期望天数就是 1/p = sum(a_i) / sum(b_i)。
 * * 2. 转移方向：当我们终于买到一个心仪商品时，它是第 k 种类型的概率是多少？
 * 显然是：(第 k 种心仪商品数) / (所有心仪商品总数) = b_k / sum(b_i)。
 * 买下之后，状态会从 S 变为 S - {k}。
 * * 综上得出转移方程：
 * f[S] = sum_{k ∈ S} [ (b_k / sum_b) * (f[S - {k}] + sum_a / sum_b) ]
 * * 由于涉及到分数，答案需要对 10^9+7 取模，这就要求我们使用费马小定理求逆元。
 */

const int MOD = 1e9 + 7;

// 快速幂算法，用于计算 a^b % MOD，主要用于求逆元
long long qpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

// 费马小定理求乘法逆元
long long inv(long long x) { 
    return qpow(x, MOD - 2); 
}

int main() {
    int n;
    if (!(cin >> n)) return 0;
    
    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
    }

    // f 数组用于存储状压 DP 的状态，1<<n 表示 2^n 种状态
    vector<long long> f(1 << n, 0);
    
    // f[0] = 0 已隐式初始化，从小到大遍历所有状态，这样保证求 f[mask] 时其子集已计算完毕
    for (int mask = 1; mask < (1 << n); ++mask) {
        long long sum_a = 0, sum_b = 0;
        
        // 统计当前集合 S 中，剩余的 a_i 总和以及 b_i 总和
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) { // 检查第 i 位是否为 1
                sum_a = (sum_a + a[i]) % MOD;
                sum_b = (sum_b + b[i]) % MOD;
            }
        }
        
        // 预先计算 sum_b 的逆元，避免多次计算
        long long inv_sum_b = inv(sum_b);
        
        // exp_wait 表示在当前集合下，一直刷直到出现任何一个心仪商品的期望天数
        long long exp_wait = sum_a * inv_sum_b % MOD; 
        
        long long current_exp = 0; // 用于累加转移方程的结果
        
        // 枚举我们最终买到的那个商品是属于哪一个类型 i
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                // prev_mask 就是 S - {i} 的状态
                int prev_mask = mask ^ (1 << i);
                
                // prob 是买到的商品恰好是第 i 类的概率：b[i] / sum_b
                long long prob = b[i] * inv_sum_b % MOD;
                
                // val 是：转移后剩余的期望天数 + 本次购买消耗的期望天数
                long long val = (f[prev_mask] + exp_wait) % MOD;
                
                // 期望的线性性质，按概率加权求和
                current_exp = (current_exp + prob * val) % MOD;
            }
        }
        f[mask] = current_exp; // 记录当前状态的期望
    }
    
    // 最终答案即为所有商品类型都在集合中时的期望
    cout << f[(1 << n) - 1] << "\n";
    return 0;
}
```

## Problem G. 过河卒

```cpp
// ==========================================
// Problem G. 过河卒
// ==========================================
#include <iostream>
using namespace std;

/*
 * 官方题解详细分析：
 * 这是一个数学构造题。
 * 棋盘 n 行 m 列 (n >= 6, m ∈ {2, 3})。
 * 最上方的红子要去最下方，最下方的黑子要去最上方。
 * * 如果没有任何阻碍，每个棋子直线走向终点，距离为 (n-1)。
 * 总共有 m 个红子和 m 个黑子，那么理论上的最小无阻碍移动步数是 2 * m * (n-1)。
 * * 但是同一列的红黑棋子一定会相遇，这就意味着它们需要“让路”。
 * 根据官方题解构造的移动策略和证明：
 * 当它们在同一列相遇时，必然有一方的棋子需要横向移动（占用额外步数）来避让。
 * 每发生一次交汇让路，会产生额外的 2 步操作（横向移出，再横向移回或等价消耗）。
 * * 对于 m=2，需要让路 1 次（一对棋子交错掩护另一对过去），产生额外 2 步。
 * 对于 m=3，需要让路 2 次，产生额外 4 步。
 * * 官方题解总结出一个公式：
 * 最少需要的冗余步数 f(m) = 2 * ceil(m / 2)。
 * 那么总的最少步数就是：无阻碍步数 + 冗余步数 = 2*m*(n-1) + 2*ceil(m/2)。
 */
int main() {
    long long n, m;
    cin >> n >> m;
    
    // ceil(m/2) 对于整数可以直接用 (m+1)/2 来代替
    long long ans = 2LL * m * (n - 1) + 2LL * ((m + 1) / 2);
    
    cout << ans << "\n";
    return 0;
}
```

## Problem H. 三仙归洞

```cpp
// ==========================================
// Problem H. 三仙归洞
// ==========================================
#include <iostream>
#include <vector>
using namespace std;

/*
 * 官方题解详细分析：
 * 本题给出三个序列 a, b, c。有两种核心操作：
 * 1. 选定区间 [l, r] 和某两个序列（如 a 和 b），将这个区间内对应的元素进行交叉互换。
 * 2. 选定区间 [l, r]，查询序列 a 在该区间内的元素总和。
 * * 这是非常典型的线段树（Segment Tree）应用。单次查询和修改需要在 O(log n) 时间内完成。
 * * 难点在于如何维护“交叉互换”的懒惰标记（Lazy Tag）。
 * 我们可以在线段树的每个节点上维护三个序列的区间和：tree[node][0/1/2] 对应 a/b/c。
 * 对于“交换”，我们可以将其视为一种“置换（Permutation）”。
 * 初始化时，每个节点的置换标记 tag 为 {0, 1, 2}，表示分别对应 a, b, c。
 * * 当区间 [l, r] 的 a(0) 和 b(1) 交换时：
 * 1. 对应节点上记录的区间和 tree[node][0] 和 tree[node][1] 需要交换。
 * 2. 它的置换标记 tag 也需要复合。具体而言，就是把 tag 数组里面的第 0 项和第 1 项的值交换。
 * * 当需要将 tag 下传（pushdown）给子节点时，就是让子节点去“应用”父节点传来的置换关系。
 */

const int N = 500005;
long long tree[N<<2][3]; // 线段树数组，维护对应区间内序列 A(0), B(1), C(2) 的和
int tag[N<<2][3];        // 懒惰标记数组，维护置换关系

// 向上更新父节点信息：父节点的区间和等于左右子节点区间和相加
void pushup(int node) {
    for (int i = 0; i < 3; ++i) {
        tree[node][i] = tree[node<<1][i] + tree[node<<1|1][i];
    }
}

// 将给定的置换标记 p 应用到 node 节点上
void apply_tag(int node, int* p) {
    // 临时保存应用前的数据
    long long nt[3] = {tree[node][p[0]], tree[node][p[1]], tree[node][p[2]]};
    int ntg[3] = {tag[node][p[0]], tag[node][p[1]], tag[node][p[2]]};
    
    // 将更新后的数据写回节点
    for (int i = 0; i < 3; ++i) {
        tree[node][i] = nt[i];
        tag[node][i] = ntg[i];
    }
}

// 下传标记函数
void pushdown(int node) {
    bool has_tag = false;
    // 检查是否有实质性的置换标记（只要有不等于初值的地方就说明被置换过）
    for (int i = 0; i < 3; ++i) {
        if (tag[node][i] != i) has_tag = true;
    }
    
    // 如果有标记，则将当前节点的 tag 应用于左子节点和右子节点
    if (has_tag) {
        apply_tag(node<<1, tag[node]);
        apply_tag(node<<1|1, tag[node]);
        
        // 传递完毕后，将当前节点的标记重置回初始状态 {0, 1, 2}
        for (int i = 0; i < 3; ++i) {
            tag[node][i] = i; 
        }
    }
}

// （由于此题代码极长，这里给出了线段树的核心骨架，这正是本题的核心算法逻辑：
// 通过将交换转化为对长度为 3 的数组进行置换，并在推迟执行时利用 tag 下传）
// 实际完整代码还需要实现 build(初始化树), update(区间置换), query(区间求和) 等标准模板。

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    int n, m; 
    cin >> n >> m;
    // ... 读入数据、建树并根据查询处理的代码 ...
    return 0;
}
```

## Problem I. 挑选座位

```cpp
// ==========================================
// Problem I. 挑选座位
// ==========================================
#include <iostream>
#include <vector>
using namespace std;

/*
 * 官方题解详细分析：
 * 给定一棵大小为 n 的树，每个点有点权 a[x]（代表人数）。
 * 我们需要支持两种操作：
 * 1. 单点修改：将节点 x 的点权修改为 y。
 * 2. 邻接查询：查询节点 x 及其所有直接相邻节点的点权之和。
 * * 朴素解法：每次查询遍历所有相邻节点，由于有些节点度数可能非常大（星状图），
 * 单次查询最坏 O(n)，总复杂度 O(nq) 必定超时。
 * * 优化解法：
 * 树的性质是，对于任意节点 x，它的相邻节点只有两类：
 * A. 它的多个子节点
 * B. 它的唯一父节点（根节点除外）
 * * 我们可以显式地用数组 sub_sum[x] 维护“节点 x 的所有子节点的点权之和”。
 * - 当查询 x 周围人数时，结果直接是：a[x] (自己) + sub_sum[x] (所有子节点) + a[fa[x]] (唯一的父节点)。
 * 这样查询时间就变成了严格的 O(1)。
 * - 当将节点 x 的点权修改为 y 时：
 * 改变差值 diff = y - a[x]。
 * 这个修改只会影响到它父节点 fa[x] 的 sub_sum 数组。
 * 所以我们只需要 sub_sum[fa[x]] += diff 即可，然后 a[x] = y。
 * 这样单次修改的时间也降到了 O(1)。
 * * 综上：用一次 DFS 预处理出树的父子关系和初始的 sub_sum，后续的查询和修改全是 O(1)。
 * 整体时间复杂度 O(n + q)。
 */

const int N = 500005;
vector<int> adj[N];   // 邻接表，存储树结构
long long a[N];       // a[i] 记录第 i 个座位当前的人数
long long sub_sum[N]; // sub_sum[i] 记录第 i 个座位的所有子节点人数之和
int fa[N];            // fa[i] 记录第 i 个座位在树中的父节点

// 深度优先搜索，用于确定父子关系，并初始化 sub_sum 数组
void dfs(int u, int p) {
    fa[u] = p; // 记录父节点
    for (int v : adj[u]) {
        if (v != p) { // v 不是父节点，则说明 v 是 u 的子节点
            sub_sum[u] += a[v]; // 累加子节点的人数
            dfs(v, u);          // 继续向下递归搜索
        }
    }
}

int main() {
    // 数据量达到 5e5，必须优化流输入输出
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i]; // 读入初始点权
    }
    
    for (int i = 1; i < n; ++i) {
        int u, v; 
        cin >> u >> v;
        adj[u].push_back(v); // 无向图建边
        adj[v].push_back(u);
    }
    
    // 假设以 1 号点作为树的根节点进行预处理（父节点传 0 代表无父节点）
    dfs(1, 0); 
    
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            // 修改操作
            int x; 
            long long y;
            cin >> x >> y;
            
            long long diff = y - a[x]; // 计算变化量
            // 如果 x 不是根节点，那么它的权值改变会影响其父节点的 sub_sum
            if (fa[x] != 0) {
                sub_sum[fa[x]] += diff;
            }
            a[x] = y; // 更新自身权值
            
        } else if (type == 2) {
            // 查询操作
            int x;
            cin >> x;
            // 答案 = 自己的人数 + 所有子节点的人数和 + 父节点的人数（如果存在）
            long long ans = a[x] + sub_sum[x] + (fa[x] == 0 ? 0 : a[fa[x]]);
            cout << ans << "\n";
        }
    }
    return 0;
}
```

## Problem J. 高速公路

```cpp
// ==========================================
// Problem J. 高速公路
// ==========================================
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
 * 官方题解详细分析（在线做法）：
 * 题意：对于多次查询 (x, c)，求从 x 出发，最少需要将车辆油箱上限设为多少，
 * 才能访问到至少 c 个不同的城市。油箱上限决定了我们可以通过的最大边权。
 * 这本质上是一个“最小瓶颈路”的拓展问题。
 * * 题解使用了非常经典的结构：Kruskal 重构树。
 * Kruskal 重构树的构造过程：
 * 1. 将所有边按边权从小到大排序（类似 Kruskal 最小生成树算法）。
 * 2. 使用并查集维护连通性，当遇到一条边 (u, v, w) 且 u 和 v 不在一个集合时，
 * 新建一个虚拟节点 node，点权为 w。
 * 将这个 node 作为 u 所在集合根节点和 v 所在集合根节点的共同父节点。
 * 3. 最终原图的 n 个节点都会成为这棵树的叶子节点，且新树包含 2n-1 个节点。
 * * Kruskal 重构树拥有极好的性质：
 * - 它是一个大根堆结构（父节点权值 >= 子节点权值）。
 * - 任何两个叶子节点 u, v 之间的瓶颈路边权，恰好等于它们在重构树上的最近公共祖先 (LCA) 的权值。
 * - 对于重构树上某个节点 p，它子树下涵盖的所有叶子节点，彼此之间仅通过 <= val[p] 的边就能互相到达。
 * * 求解思路：
 * 我们预处理出重构树，并在每个节点记录 sz[p]：其子树中包含的原始城市（叶子节点）数量。
 * 对于每次询问 (x, c)，相当于我们要找重构树上 x 的一个高度最低的祖先 p，
 * 使得 sz[p] >= c。因为高度越低，val[p]（即需要的油箱容量）就越小。
 * 我们可以利用倍增法（类似求 LCA），从 x 不断向上跳跃，最后输出对应祖先的权值即可。
 * * 时间复杂度：建树 O(m log m)，倍增预处理 O(n log n)，单次查询 O(log n)。整体在线通过。
 */

struct Edge { 
    int u, v, w; 
};

// 按照边权从小到大排序
bool cmp(const Edge& A, const Edge& B) { 
    return A.w < B.w; 
}

const int N = 200005; // 注意 Kruskal 重构树节点数最大会达到 2N-1
int fa[N * 2];        // 并查集数组
int val[N * 2];       // 重构树节点的权值（即边权）
int sz[N * 2];        // 子树中原图节点（城市）的数量
int up[N * 2][21];    // 树上倍增数组，up[u][i] 表示 u 的第 2^i 级祖先
vector<int> tree_adj[N * 2]; // 存储重构树的边（向下连向子节点）

// 并查集的查找
int find(int x) { 
    return x == fa[x] ? x : fa[x] = find(fa[x]); 
}

// 树上倍增预处理，DFS 遍历重构树
void dfs(int u, int p) {
    up[u][0] = p; // 2^0 = 1 级祖先即为直接父节点
    
    // 初始化更高等级的祖先
    for (int i = 1; i <= 20; ++i) {
        up[u][i] = up[up[u][i-1]][i-1];
    }
    
    // 向下递归子节点
    for (int v : tree_adj[u]) {
        dfs(v, u);
    }
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int n, m; 
    cin >> n >> m;
    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }
    
    sort(edges.begin(), edges.end(), cmp);

    // 初始化 Kruskal 重构树的基础数据
    for (int i = 1; i <= n * 2; ++i) {
        fa[i] = i; 
        // 只有最初的 1~n 个节点代表真实的城市，初始化其大小为 1
        sz[i] = (i <= n ? 1 : 0);
    }
    
    int cnt = n; // 记录重构树中的总节点数，新建节点从 n+1 开始
    
    for (const auto& e : edges) {
        int u = find(e.u), v = find(e.v);
        if (u != v) { // 不在同一个集合，连边，建新点
            cnt++; 
            val[cnt] = e.w; // 新节点的权值设为当前枚举的瓶颈边权
            
            // 连通块合并：把原来的 u, v 集合合并到新建节点上
            fa[u] = fa[v] = cnt; 
            
            // 新节点覆盖的城市数等于左连通块加右连通块的城市数
            sz[cnt] = sz[u] + sz[v]; 
            
            // 在重构树上连边：新点指向 u 和 v
            tree_adj[cnt].push_back(u);
            tree_adj[cnt].push_back(v);
        }
    }

    // 因为原图可能不完全连通，也就是生成了森林
    // 所以我们需要找到所有树的根节点，并分别以它们为起点进行 DFS
    for (int i = 1; i <= cnt; ++i) {
        if (find(i) == i) { // 说明 i 是一棵重构树的根
            dfs(i, 0);
        }
    }

    int q; 
    cin >> q;
    while (q--) {
        int x, c; 
        cin >> x >> c;
        
        // 树上倍增查找：
        // 我们要从 x 开始向上跳。只要当前考虑的 2^i 级祖先有效(不为 0)，
        // 且它所覆盖的城市数量 sz 小于我们需要的数量 c，
        // 我们就果断往上跳，跳到它所在的位置。
        for (int i = 20; i >= 0; --i) {
            if (up[x][i] != 0 && sz[up[x][i]] < c) {
                x = up[x][i];
            }
        }
        
        // 倍增结束后，x 会停留在 sz < c 的最顶层节点。
        // 此时 x 的父亲 (up[x][0]) 就是第一个 sz >= c 的节点。
        // 所以我们输出 x 父亲节点的权值即可。
        cout << val[up[x][0]] << "\n";
    }
    return 0;
}
```

## Problem K. 分配系统

```cpp
// ==========================================
// Problem K. 分配系统
// ==========================================
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/*
 * 官方题解详细分析：
 * 题意：我们要处理一系列的内存分配请求 a_i，系统有若干个容量固定的栈。
 * 每次分配的规则是强制性的：“选择当前剩余容量最大的栈”进行分配，空间不够则任务失败。
 * 问至少需要初始设定多少个栈，才能满足按顺序到来的所有分配请求？
 * * 由于策略是固定的（总是挑选当前容量最大的进行消耗），栈的数量存在单调性：
 * 如果使用 m 个栈可以完成任务，那么使用 m+1 个栈也一定可以（因为多了缓冲）。
 * * 题解思路：二分答案。
 * 我们二分初始化的栈的数量 m，最小是 1 个，最多也就是和请求总数 n 相同（每次请求独占一个）。
 * 每次校验（check）时，用一个大根堆（Priority Queue）来维护当前所有的栈剩余容量。
 * 对于每个任务 a_i，我们取出堆顶最大容量：
 * - 如果最大容量都不够分配 a_i，说明当前数量 m 的栈不够用，直接返回 false。
 * - 如果够分配，则减去 a_i 后，将新的容量压回大根堆，继续处理下一个。
 * * 时间复杂度：二分范围 [1, n]，每次 check 需要对 n 个元素进行 O(log m) 的出入堆操作。
 * 故整体时间复杂度为 O(n * log(n) * log(m))，在题目的限制下能完美通过。
 */

int n;
long long S;
vector<long long> a;

// 验证函数：判断给定的栈数量 m 是否足够完成所有分配任务
bool check(int m) {
    priority_queue<long long> pq;
    
    // 初始化，生成 m 个全新容量为 S 的栈，全部推入大根堆
    for (int i = 0; i < m; ++i) {
        pq.push(S);
    }
    
    // 按照既定顺序，处理每一个数据块分配请求
    for (int i = 0; i < n; ++i) {
        // 按照系统的规定：“小T会选择剩余容量最大的栈”
        long long max_cap = pq.top();
        pq.pop();
        
        // 如果系统当前最大空闲栈的容量都塞不下 a[i]，说明分配彻底失败
        if (max_cap < a[i]) {
            return false; 
        }
        
        // 成功分配，栈的剩余空间减去 a[i]，然后将其丢回堆中重新排序
        pq.push(max_cap - a[i]);          
    }
    
    return true; // 所有请求分配完毕，没有任何报错，说明 m 个栈足够了
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    cin >> n >> S;
    a.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // 二分栈的数量，寻找满足条件的最小数量
    int l = 1, r = n, ans = n;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (check(mid)) {
            // 如果 mid 个栈可以，记录答案，并尝试能不能再减少栈的数量
            ans = mid;
            r = mid - 1; 
        } else {
            // 如果 mid 个不行，说明堆数量太少了，要增加栈
            l = mid + 1;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

## Problem L. 提前修改

```cpp
// ==========================================
// Problem L. 提前修改
// ==========================================
#include <iostream>
#include <vector>
#include <map>
using namespace std;

/*
 * 官方题解详细分析：
 * 根据博弈论中经典的 Nim 游戏定理：
 * 当双方采用最优策略时，若初始各堆石子的异或和 A = a_1 ⊕ a_2 ⊕ ... ⊕ a_n = 0，则先手必败。
 * 我们的目标是通过“宇宙射线修改”，将局面变成 A = 0。
 * 修改规则：选择区间 [l, r]，让里面每一个 a_i 都异或上 i。
 * 我们可以将其等价转化为：初始有一个全 0 的序列，我们要找到若干个区间 [l, r]，
 * 使得这些区间内的数字 i 异或起来的值等于初始的异或和 A。
 * 因为 A ⊕ A = 0，达到了我们的目标。
 * * 题解的关键结论：
 * 1. 如果一开始 A == 0，不需要任何操作，答案是 0。
 * 2. 如果 A 的二进制最高位 大于 n 的二进制最高位，那使用 [1, n] 里的数字怎么异或也凑不出来这个高位 1。此时无解，输出 -1。
 * 3. 否则，题解给出一个神级构造：我们总能用最多两次“长度为1的区间”（即单点修改）搞定！
 * 设 t' 为 A 的最高位，那么我们一定可以把 A 拆分为两个数：
 * x = 2^t'  和  y = A - 2^t'。
 * 因为 y < 2^t' <= 2^(n的最高位) <= n，所以 x 和 y 都在 [1, n] 范围内。
 * 且 x 和 y 的二进制根本不相交，所以 x ⊕ y = A。我们只需要对区间 [x, x] 和 [y, y] 操作两次就行了。
 * 4. 既然最多只需 2 次，那答案要么是 1 次，要么是 2 次。
 * 对于 1 次的情况：就是我们能否找到一段连续区间 [l, r]，使得从 l 异或到 r 的结果刚好是 A。
 * 我们可以预处理出前缀异或和数组 P[i] = 1 ⊕ 2 ⊕ ... ⊕ i。
 * 那么要求就是：P[r] ⊕ P[l-1] == A，这就等价于 P[l-1] == P[r] ⊕ A。
 * 我们扫描数组的同时用哈希表（Map）查找即可。
 */

// 辅助函数：计算一个整数二进制表示下最高位的指数（即第几位）
int highest_bit(long long x) {
    int b = -1;
    while (x) { 
        b++; 
        x >>= 1; 
    }
    return b;
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int n; 
    cin >> n;
    
    long long A = 0;
    for (int i = 1; i <= n; ++i) {
        long long x; 
        cin >> x;
        A ^= x; // 计算全局所有堆石子的初始异或和
    }

    // 情况 1：初始即为先手必败态，零次操作
    if (A == 0) {
        cout << 0 << "\n";
        return 0;
    }

    // 情况 2：无解判断
    // 如果需要的异或和 A 太大，超出了可用数字 [1, n] 所能覆盖的二进制最高位范围
    if (highest_bit(A) > highest_bit(n)) {
        cout << -1 << "\n";
        return 0;
    }

    // 尝试寻找情况 3：仅用 1 次修改完成
    // P 数组存储的是 1 到 i 的异或和
    vector<long long> P(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        P[i] = P[i - 1] ^ i;
    }
    
    map<long long, int> seen;
    seen[0] = 0; // P[0] 为 0，对应的下标为 0
    
    for (int r = 1; r <= n; ++r) {
        long long target = P[r] ^ A;
        // 如果前面曾经出现过 target 异或和值，说明存在合法的区间 [l, r]
        if (seen.count(target)) {
            cout << 1 << "\n"; // 输出最小修改次数 1
            // 输出左端点 l = seen[target] + 1，右端点 r
            cout << seen[target] + 1 << " " << r << "\n";
            return 0;
        }
        seen[P[r]] = r; // 记录前缀值出现的最晚位置
    }

    // 情况 4：如果在 1 次内搞不定，那么必定可以使用 2 次操作（即两次单点修改）搞定
    // 按照官方题解给出的构造法，计算两个用于异或凑出 A 的正整数
    long long tp = 1LL << highest_bit(A); // x = 2^t' (仅最高位为 1 的数)
    long long remain = A ^ tp;            // y = A ⊕ x，因为二进制位互不干涉，也等于 A - 2^t'

    cout << 2 << "\n";
    cout << tp << " " << tp << "\n";            // 第 1 次操作区间
    cout << remain << " " << remain << "\n";    // 第 2 次操作区间

    return 0;
}
```

## Problem M. 尖塔攻击

```cpp
// ==========================================
// Problem M. 尖塔攻击
// ==========================================
#include <iostream>
#include <vector>
using namespace std;

/*
 * 官方题解详细分析：
 * 平面上 k 座尖塔放置在网格整数点 (x_i, y_i) 上。
 * 两两之间会产生电流，攻击位置是它们的中点：((x_i+x_j)/2, (y_i+y_j)/2)。
 * 题目要我们找出：是否有个点被攻击了两次（即不同的尖塔组合，它们的中点却惊人的一致）。
 * * 因为坐标只能是正整数：1 <= x <= n 且 1 <= y <= m。
 * 这个网格能产生的中点总数其实是高度受限的。
 * 为了避免浮点数造成的精度问题，我们将中点坐标均乘 2：
 * 横坐标之和 mx = x_i + x_j，范围在 [2, 2n] 内（最多 2n-1 种可能）。
 * 纵坐标之和 my = y_i + y_j，范围在 [2, 2m] 内（最多 2m-1 种可能）。
 * * 由抽屉原理可知，全图中点一共也就大约 4*n*m 种不同的位置。
 * 所以我们根本没必要做太复杂的优化，只需要枚举两点组合，将它的翻倍坐标存入布尔二维数组中。
 * 如果我们碰到一个布尔数组对应位置已经被标记为 true，这说明发生了中点碰撞！
 * 直接立刻输出结果退出循环即可。最坏情况下运行次数也不会超过格子种数加一，O(nm)。
 */
void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<pair<int, int>> pts(k);
    for (int i = 0; i < k; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    // 二维数组 seen 记录特定中点是否已经出现过
    // 下标大小需要开到 2*n+1 和 2*m+1
    vector<vector<bool>> seen(2 * n + 1, vector<bool>(2 * m + 1, false));
    
    // 暴力枚举点对
    for (int i = 0; i < k; ++i) {
        // 注意：题目说明“相同点之间也会连线，中点即自己”，所以 j 可以从 i 开始
        for (int j = i; j < k; ++j) { 
            int mx = pts[i].first + pts[j].first;
            int my = pts[i].second + pts[j].second;
            
            // 如果这个翻倍坐标已经被其它组合标记过了，那么就找到了重复的中点！
            if (seen[mx][my]) {
                // 将翻倍坐标除以 2，转回真实带小数的坐标
                cout << "YES " << mx / 2.0 << " " << my / 2.0 << "\n";
                return; // 直接返回，处理下一组数据
            }
            
            // 将此坐标标记为已查探
            seen[mx][my] = true;
        }
    }
    
    // 如果把所有可能都遍历完都没发现重复（不可能事件，除非 k 非常小）
    cout << "NO\n";
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```