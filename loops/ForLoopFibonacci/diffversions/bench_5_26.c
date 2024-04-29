#include <stdio.h>

#define STEP   5
#define ITERS   26

__attribute__ ((noinline))
int looptarget() { 
    int fib1 = 0, fib2 = 1;
    int sum = fib1; // Start sum with the first Fibonacci number only
    for (int iter = 0; iter < ITERS; iter++) {
        int nextFib = fib1 + fib2;
        fib1 = fib2;
        fib2 = nextFib;
           // Add to sum only if the current index is a multiple of STEP
        sum += nextFib + STEP;
        
    }
    return sum;
}

int main(int argc, char* argv[]) {

   int t=looptarget();
   printf("Result %d",t);
}
