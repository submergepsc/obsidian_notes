#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int count_unsafe = 0;
int count_safe = 0;

void* runner() {
    for(int i = 0; i < 1000000; i++) {
        count_unsafe++;
    }
    return 0;
}

void* runner_sync() {
    for(int i = 0; i < 1000000; i++) {
        __sync_fetch_and_add(&count_safe, 1);
    }
    return 0;
}

int main() {
    pthread_t threadIDs[32];
    for(int i = 0; i < 32; i+=2) {
        pthread_create(&threadIDs[i], NULL, runner_sync, NULL);
        pthread_create(&threadIDs[i+1], NULL, runner, NULL);
    }
    for(int i = 0; i < 32; i++) {
        pthread_join(threadIDs[i], NULL);
    }

    printf("The atomic counter is %u\n", count_safe);
    printf("The non-atomic counter is %u\n", count_unsafe);
}