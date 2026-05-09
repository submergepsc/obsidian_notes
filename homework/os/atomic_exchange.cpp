#include <iostream>
#include <pthread.h>
#include <atomic>


std::atomic<bool> ready (false);
std::atomic<bool> winner (false);

void* count1m (void *arg) {
    int id = *(int*)arg;
    while (!ready) {}                  // wait for the ready signal
    for (int i=0; i<1000000; ++i) {}   // go!, count to 1 million
    if (!winner.exchange(true)) {
        std::cout << "thread #" << id << " won!\n";
    }
    return NULL;
};

int main ()
{
    pthread_t threadIDs[10];
    int ids[10];
    std::cout << "spawning 10 threads that count to 1 million..." << std::endl;
    for(int i = 0; i < 10; i++) {
        ids[i] = i;
        pthread_create(&threadIDs[i], NULL, count1m, (void*)&ids[i]);
    }
    ready = true;
    for(int i = 0; i < 10; i++) {
        pthread_join(threadIDs[i], NULL);
    }

    return 0;
}