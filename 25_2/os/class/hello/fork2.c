#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

void main() {
    int a = 0;
    int rc = fork();
    a++;
    if (rc == 0) {
        rc = fork();
        a++;
    } else {
        a++;
    }
    printf("Hello pid: %d !\n", rc);
    printf("a is %d\n", a);

    int status;
    wait(&status);
}