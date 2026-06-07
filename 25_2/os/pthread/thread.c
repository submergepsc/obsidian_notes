#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
volatile int balance = 0;
void *mythread(void *arg) {
    int i;
    for (i = 0; i < 20000; i++) {
        balance++;
    }
    printf("Balance is % d\n", balance);
    return NULL;
}
int main(int argc, char *argv[]) {
    pthread_t p1, p2, p3;
    pthread_create(&p1, NULL, mythread, (void*)"A");
    pthread_create(&p2, NULL, mythread, (void*)"B");
    pthread_create(&p3, NULL, mythread, (void*)"C");
    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);
    printf("Final Balance is % d\n", balance);
}
