#include <stdio.h>

#define STEP   5
#define ITERS   9

__attribute__ ((noinline))
int looptarget() {
 int iter;
 int sum = 0;
    for(int iter = 0; iter < ITERS; ++iter) {
        if(iter % 2 == 0) { // Only add on even iterations
            sum += 3*STEP;
        } else {
            sum -= STEP; // Subtract on odd iterations
        }
    }
    return sum;
}

int main(int argc, char* argv[]) {
   int t=looptarget();
   printf("Result %d",t);
}
