#include <stdio.h>
static int global_counter = 7;
const char message[] = "hello from an ELF executable";
static int add(int a, int b)
{
    return a + b;
}
int main(void)
{
    int local_value = add(global_counter, 35);
    printf("%s\n", message);
    printf("global_counter=%d local_value=%d\n", global_counter, local_value);
    printf("function main=%p add=%p\n", (void *)main, (void *)add);
    return 0;
}
