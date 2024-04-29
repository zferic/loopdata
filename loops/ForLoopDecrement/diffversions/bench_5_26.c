#include <stdio.h>

#define STEP 5   // Starting step value
#define ITERS 32

__attribute__ ((noinline))
int looptarget() {
    int iter;
    int sum = 0;
    int step = STEP;
    for (iter = 0; iter < ITERS; ++iter) {
        sum += step;
        if (step > 1) {  // Ensure step does not become less than 1
            step -= 1;  // Decrement the step by 1 each iteration
        }
    }
    return sum;
}

int main(int argc, char* argv[]) {
    int t = looptarget();
    printf("Result %d", t);
}