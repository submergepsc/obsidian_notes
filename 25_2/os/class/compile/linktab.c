// linked_list.c
#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;            // offset = 0, size = 4
                         // 4 字节填充（padding），保证 next 的 8 字节对齐
    struct Node *next;   // offset = 8, size = 8
};
// sizeof(struct Node) = 16
int list_sum(struct Node *head) {
    int sum = 0;
    while (head != NULL) {
        sum += head->data;
        head = head->next;
    }
    return sum;
}
