#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <stdatomic.h>

static _Atomic long counter = 0;
static long iters_per_thread;

static void *worker(void *arg) {
    (void)arg;

    for (long i = 0; i < iters_per_thread; i++) {
        atomic_fetch_add_explicit(&counter, 1, memory_order_relaxed);
    }

    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "usage: %s <n_threads> <iters_per_thread>\n", argv[0]);
        return 1;
    }

    int n_threads = atoi(argv[1]);
    iters_per_thread = atol(argv[2]);

    pthread_t *tids = malloc(sizeof(pthread_t) * n_threads);
    if (tids == NULL) {
        perror("malloc");
        return 1;
    }

    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int i = 0; i < n_threads; i++) {
        pthread_create(&tids[i], NULL, worker, NULL);
    }

    for (int i = 0; i < n_threads; i++) {
        pthread_join(tids[i], NULL);
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    long final_counter = atomic_load_explicit(&counter, memory_order_relaxed);
    long expected = (long)n_threads * iters_per_thread;

    double elapsed =
        (end.tv_sec - start.tv_sec) +
        (end.tv_nsec - start.tv_nsec) / 1000000000.0;

    printf("expected = %ld, counter = %ld, lost = %ld, time = %.6f\n",
           expected, final_counter, expected - final_counter, elapsed);

    free(tids);
    return 0;
}