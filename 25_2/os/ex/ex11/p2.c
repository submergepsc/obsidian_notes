#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>

#define NUM_PHILOSOPHERS 5

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
bool forks[NUM_PHILOSOPHERS]; 

void* philosopher(void* num) {
    int id = *(int*)num;
    int left = id;
    int right = (id + 1) % NUM_PHILOSOPHERS;

    while (1) {
        printf("Philosopher %d is thinking.\n", id);
        usleep(10000);

        pthread_mutex_lock(&mutex);
        // 等待左右叉子都可用
        while (!forks[left] || !forks[right]) {
            pthread_cond_wait(&cond, &mutex);
        }

        forks[left] = false;
        forks[right] = false;
        printf("Philosopher %d starts eating.\n", id);
        pthread_mutex_unlock(&mutex);

        usleep(10000); 

        pthread_mutex_lock(&mutex);
        forks[left] = true;
        forks[right] = true;
        printf("Philosopher %d finished eating.\n", id);
        pthread_cond_broadcast(&cond); // 唤醒等待的哲学家
        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}

int main() {
    pthread_t philosophers[NUM_PHILOSOPHERS];
    int ids[NUM_PHILOSOPHERS];
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        forks[i] = true; // 初始化叉子可用
        ids[i] = i;
        pthread_create(&philosophers[i], NULL, philosopher, &ids[i]);
    }
    for (int i = 0; i < NUM_PHILOSOPHERS; i++)
        pthread_join(philosophers[i], NULL);
}