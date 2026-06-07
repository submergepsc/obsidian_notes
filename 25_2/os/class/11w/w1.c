#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>
#define BUFFER_SIZE 10
#define NUM_PRODUCERS 3
#define NUM_CONSUMERS 3
#define NUM_ITEMS 1000000  // 增加处理的数据量以便测试
// 性能统计
struct {
    long long total_produced;
    long long total_consumed;
    long long producer_wait_time;
    long long consumer_wait_time;
    struct timeval start_time;
    struct timeval end_time;
} stats = {0};
// 共享资源
int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int count = 0;
// 同步原语
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t not_full = PTHREAD_COND_INITIALIZER;
pthread_cond_t not_empty = PTHREAD_COND_INITIALIZER;
// 获取当前时间（微秒）
long long get_time_us() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec * 1000000LL + tv.tv_usec;
}
// 生产者函数
void* producer(void* arg) {
    int producer_id = *(int*)arg;
    int item;
    long long wait_start;
    for (int i = 0; i < NUM_ITEMS; i++) {
        item = rand() % 100;
        pthread_mutex_lock(&mutex);
        while (count == BUFFER_SIZE) {
            wait_start = get_time_us();
            pthread_cond_wait(&not_full, &mutex);
            stats.producer_wait_time += get_time_us() - wait_start;
        }
        buffer[in] = item;
        in = (in + 1) % BUFFER_SIZE;
        count++;
        stats.total_produced++;
        pthread_cond_signal(&not_empty);
        pthread_mutex_unlock(&mutex);
        usleep(1);  // 最小延时
    }
    return NULL;
}
// 消费者函数
void* consumer(void* arg) {
    int consumer_id = *(int*)arg;
    int item;
    long long wait_start;
    for (int i = 0; i < NUM_ITEMS; i++) {
        pthread_mutex_lock(&mutex);
        while (count == 0) {
            wait_start = get_time_us();
            pthread_cond_wait(&not_empty, &mutex);
            stats.consumer_wait_time += get_time_us() - wait_start;
        }
        item = buffer[out];
        out = (out + 1) % BUFFER_SIZE;
        count--;
        stats.total_consumed++;
        pthread_cond_signal(&not_full);
        pthread_mutex_unlock(&mutex);
        usleep(1);  // 最小延时
    }
    return NULL;
}
void print_stats() {
    long long total_time = (stats.end_time.tv_sec - stats.start_time.tv_sec) * 1000000LL +
                          (stats.end_time.tv_usec - stats.start_time.tv_usec);
    printf("\n性能测试结果:\n");
    printf("总运行时间: %.2f 秒\n", total_time / 1000000.0);
    printf("总生产数量: %lld\n", stats.total_produced);
    printf("总消费数量: %lld\n", stats.total_consumed);
    printf("生产者等待时间: %.2f 秒\n", stats.producer_wait_time / 1000000.0);
    printf("消费者等待时间: %.2f 秒\n", stats.consumer_wait_time / 1000000.0);
    printf("每秒处理数量: %.2f\n", (stats.total_produced * 1000000.0) / total_time);
}
int main() {
    pthread_t producer_threads[NUM_PRODUCERS];
    pthread_t consumer_threads[NUM_CONSUMERS];
    int producer_ids[NUM_PRODUCERS];
    int consumer_ids[NUM_CONSUMERS];
    // 记录开始时间
    gettimeofday(&stats.start_time, NULL);
    // 创建生产者线程
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        producer_ids[i] = i + 1;
        if (pthread_create(&producer_threads[i], NULL, producer, &producer_ids[i]) != 0) {
            perror("创建生产者线程失败");
            exit(1);
        }
    }
    // 创建消费者线程
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        consumer_ids[i] = i + 1;
        if (pthread_create(&consumer_threads[i], NULL, consumer, &consumer_ids[i]) != 0) {
            perror("创建消费者线程失败");
            exit(1);
        }
    }
    // 等待所有线程结束
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        pthread_join(producer_threads[i], NULL);
    }
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        pthread_join(consumer_threads[i], NULL);
    }
    // 记录结束时间
    gettimeofday(&stats.end_time, NULL);
    // 打印性能统计
    print_stats();
    // 清理资源
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&not_full);
    pthread_cond_destroy(&not_empty);
    return 0;
} 