#include <stdio.h>
#define STEP   5  // Reduced STEP to keep the sum smaller
#define ITERS   13

__attribute__ ((noinline))
int looptarget() {
    int iter;
    int sum = 0;
    for (iter = ITERS - 1; iter >= 0; --iter) {
        sum += STEP;
    }
    return sum;
}

int main(int argc, char* argv[]) {
    int t = looptarget();
    printf("Result %d", t);
}
