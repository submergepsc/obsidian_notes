#include <atomic>
#include <cstdio>

int main() {
    printf("is lock free? %s\n", std::atomic<int>::is_always_lock_free ? "true" : "false");
    std::atomic<int> a(3);
    printf("is this lock free? %s\n", a.is_lock_free() ? "true" : "false");
    return 0;
}