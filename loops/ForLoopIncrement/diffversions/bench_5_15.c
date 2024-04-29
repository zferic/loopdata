#include <stdio.h>

#define STEP 5  // Starting step value
#define ITERS   15

__attribute__ ((noinline))
int looptarget() {
    int iter;
    int sum = 0;
    int step = STEP;
    for (iter = 0; iter < ITERS; ++iter) {
        sum += step;
        step += 1;  // Increment the step by 1 each iteration
        //if (sum > 100) break;  // Cap the sum to 100 to prevent overflow
    }
    return sum;
}

int main(int argc, char* argv[]) {
    int t = looptarget();
    printf("Result %d", t);
}