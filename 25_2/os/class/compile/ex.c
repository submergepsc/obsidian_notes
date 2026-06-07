#include <stdio.h>
int square(int x) {
    return x * x;
}
void print_result(int value) {
    printf("result = %d\n", value);
}
int main(void) {
    int a = 3;
    int b = square(a);
    puts("before printf");
    print_result(b);
    puts("after printf");
    return 0;
}
