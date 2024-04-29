#include <stdio.h>
#define STEP   5  // Moderate STEP to demonstrate the modulo
#define ITERS   31

__attribute__ ((noinline))
int looptarget() {
    int iter;
    int sum = 0;
    for (iter = 0; iter < ITERS; ++iter) {
        sum = (sum + STEP) % 100;  // Keeps sum below 100
    }
    return sum;
}

int main(int argc, char* argv[]) {
    int t = looptarget();
    printf("Result %d", t);
}