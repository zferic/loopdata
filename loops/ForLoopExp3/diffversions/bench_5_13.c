#include <stdio.h>
#include <math.h>  // Include math library for pow function
#define STEP   5   // Small base for exponential growth
#define ITERS   13  // Limit iterations to keep sum within bounds

__attribute__ ((noinline))
int looptarget() {
    int iter;
    int sum = 0;
    for (iter = 0; iter < ITERS; ++iter) {
        sum += (int)pow(STEP, iter);
    }
    return sum;
}

int main(int argc, char* argv[]) {
    int t = looptarget();
    printf("Result %d", t);
}
