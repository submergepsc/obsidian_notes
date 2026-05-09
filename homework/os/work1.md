# 1.1


# 1.2
-O0 下，counter++ 被翻译成了多条指令：先从内存读取 counter 到 rax,然后对 rax 加 1,最后再把 rax 写回 counter。
而 -O2 下，编译器把循环优化成了一条加法指令：add %rax, counter
这里的 rax 存的是 iters_per_thread，相当于每个线程只对 counter 加一次总次数，而不是循环中一遍遍 counter++。因此竞争窗口变小了很多，所以你的实验里 -O2 三次运行都没有出现 lost。