#pragma GCC optimize("O2") // 开启 O2 优化，CP 标配
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

// ==========================================
// 数学工具：快速幂和求逆元
// ==========================================
// 计算 (base^exp) % MOD
long long qpow(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

// 费马小定理求逆元：在模 10^9+7 下，除以 a 等价于乘以 a^(MOD-2)
long long modInverse(long long n) {
    return qpow(n, MOD - 2);
}

int main() {
    // 优化 C++ 输入输出流，防止读写超时
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i];
    }

    // 总状态数：2^n。n最大19，1<<19 约等于 52万，空间和时间都绝对够用。
    int max_mask = 1 << n;
    
    // dp[mask] 记录状态为 mask 时的期望天数
    vector<long long> dp(max_mask, 0);
    // 预处理每个状态的 a_i 总和与 b_i 总和，避免在 DP 转移时重复循环计算
    vector<long long> sum_a(max_mask, 0);
    vector<long long> sum_b(max_mask, 0);

    // 预处理 sum_a 和 sum_b
    // 利用位运算的小技巧：mask 的总和等于 (去除了某一位的 mask 的总和) + 那一位的值
    for (int mask = 1; mask < max_mask; mask++) {
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) { // 找到 mask 中任意一个为 1 的位
                int prev_mask = mask ^ (1 << i); // 把那一位变成 0
                sum_a[mask] = sum_a[prev_mask] + a[i];
                sum_b[mask] = sum_b[prev_mask] + b[i];
                break; // 算完就跳出，O(1) 转移
            }
        }
    }

    // ==========================================
    // 核心逻辑：状压 DP (从小到大枚举状态保证拓扑序)
    // ==========================================
    for (int mask = 1; mask < max_mask; mask++) {
        long long cur_sum_a = sum_a[mask];
        long long cur_sum_b = sum_b[mask];
        
        // 计算 sum_b 的逆元
        long long inv_sum_b = modInverse(cur_sum_b);
        
        // 1. 计算第一部分：一直抽卡直到出金的“期望等待天数”
        // 对应公式的：(sum_a / sum_b)
        long long expected_wait = (cur_sum_a % MOD) * inv_sum_b % MOD;
        
        // 2. 计算第二部分：出金后，转移到下一个状态的期望
        // 对应公式的：sigma (b_k / sum_b) * f[S-{k}]
        long long expected_next = 0;
        for (int k = 0; k < n; k++) {
            if ((mask >> k) & 1) { // 如果当前状态还缺第 k 把枪的皮肤
                // 歪到 k 的概率：b_k / sum_b
                long long prob_k = (b[k] % MOD) * inv_sum_b % MOD;
                // 去掉 k 之后的新状态
                int next_mask = mask ^ (1 << k); 
                // 累加：概率 * 新状态的期望
                long long term = prob_k * dp[next_mask] % MOD;
                expected_next = (expected_next + term) % MOD;
            }
        }
        
        // 3. 把两部分加起来就是当前状态的总期望
        dp[mask] = (expected_wait + expected_next) % MOD;
    }

    // 最终答案是全集状态的期望，即所有位都为 1 的 mask
    cout << dp[max_mask - 1] << "\n";

    return 0;
}