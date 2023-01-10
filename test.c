#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// First version of rotateRight function
void rotateRight(int arr[], int size, int k) {
    for (int i = 0; i < k; i++) {
        int temp = arr[size - 1];
        for (int j = size - 1; j > 0; j--) {
            arr[j] = arr[j - 1];
        }
        arr[0] = temp;
    }
}

// Second version of rotateRight function
void rotateRight2(int arr[], int size, int k) {
    k %= size;
    int temp[k];
    for (int i = 0; i < k; i++) {
        temp[i] = arr[size - k + i];
    }
    for (int i = size - 1; i >= k; i--) {
        arr[i] = arr[i - k];
    }
    for (int i = 0; i < k; i++) {
        arr[i] = temp[i];
    }
}

int main() {
    int arr[1000];
      // use current time as seed
    srand(time(NULL));

    // fill the array with 1000 random integers
    for (int i = 0; i < 1000; i++)
    {
        arr[i] = rand();
    }

    // for (int i = 0; i < 1000; i++)
    // {
    //     printf("%d",arr[i]);
    // }
    int size = sizeof(arr) / sizeof(arr[0]);
    int k = 20;

    // Benchmark the first version of rotateRight
    clock_t start = clock();
    rotateRight(arr, size, k);
    clock_t end = clock();
    double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("First version: elapsed time = %f\n", elapsed_time);

    // Benchmark the second version of rotateRight
    start = clock();
    rotateRight2(arr, size, k);
    end = clock();
    elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Second version: elapsed time = %f\n", elapsed_time);
}