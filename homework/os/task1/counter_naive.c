#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

static long counter = 0;
static long iters_per_thread;

static void *worker(void *arg) {
    (void)arg;
    for (long i = 0; i < iters_per_thread; i++) {
        counter++;
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
    for (int i = 0; i < n_threads; i++)
        pthread_create(&tids[i], NULL, worker, NULL);
    for (int i = 0; i < n_threads; i++)
        pthread_join(tids[i], NULL);

    long expected = (long)n_threads * iters_per_thread;
    printf("expected = %ld, counter = %ld, lost = %ld\n",
           expected, counter, expected - counter);

    free(tids);
    return 0;
}
