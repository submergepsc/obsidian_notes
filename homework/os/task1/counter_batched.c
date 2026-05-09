#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

static long counter = 0;
static long iters_per_thread;
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;

static void *worker(void *arg) {
    (void)arg;

    long local = 0;

    for (long i = 0; i < iters_per_thread; i++) {
        local++;
    }

    pthread_mutex_lock(&mtx);
    counter += local;
    pthread_mutex_unlock(&mtx);

    return NULL;
}

int  main(int argc, char *argv[]) {
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

    long expected = (long)n_threads * iters_per_thread;

    double elapsed =
        (end.tv_sec - start.tv_sec) +
        (end.tv_nsec - start.tv_nsec) / 1000000000.0;

    printf("expected = %ld, counter = %ld, lost = %ld, time = %.6f\n",
           expected, counter, expected - counter, elapsed);

    free(tids);
    pthread_mutex_destroy(&mtx);

    return 0;
}
