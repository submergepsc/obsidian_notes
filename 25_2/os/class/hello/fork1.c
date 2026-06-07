#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    int x = 42;
    int rc = fork();

    if (rc < 0) {
        // fork 失败
        fprintf(stderr, "Fork failed\n");
    } else if (rc == 0) {
        // 子进程
        printf("Child process: rc is: %d; The value of x is: %d\n", rc, x);
    } else {
        // 父进程
        printf("Parent process: rc is %d; The value of x is: %d\n", rc, x);
    }
}

