#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

#define NUM_PHILOSOPHERS 5

pthread_mutex_t forks[NUM_PHILOSOPHERS];

void* philosopher(void* num) {
    int id = *(int*)num;

    int left_fork = id;
    int right_fork = (id + 1) % NUM_PHILOSOPHERS;

    while (1) {
        printf("Philosopher %d is thinking.\n", id);
        usleep(10000);  // Sleep for 0.01 seconds

        pthread_mutex_lock(&forks[left_fork]);
        printf("Philosopher %d picked up left fork.\n", id);
        pthread_mutex_lock(&forks[right_fork]);
        printf("Philosopher %d picked up right fork and starts eating.\n", id);

        usleep(10000);  // Sleep for 0.01 seconds

        pthread_mutex_unlock(&forks[right_fork]);
        printf("Philosopher %d put down right fork.\n", id);
        pthread_mutex_unlock(&forks[left_fork]);
        printf("Philosopher %d put down left fork.\n", id);
    }

    return NULL;
}

int main() {
    pthread_t philosophers[NUM_PHILOSOPHERS];
    int philosopher_numbers[NUM_PHILOSOPHERS];

    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_mutex_init(&forks[i], NULL);
        philosopher_numbers[i] = i;
    }

    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_create(&philosophers[i], NULL, philosopher, &philosopher_numbers[i]);
    }

    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_join(philosophers[i], NULL);
    }

    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_mutex_destroy(&forks[i]);
    }

    return 0;
}