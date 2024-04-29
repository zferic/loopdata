#include <stdio.h>

#define STEP   5
#define ITERS   27

//This program effectively sums all prime numbers up to a pre-defined limit (ITERS) and prints out the result.
//STEP is not used
__attribute__ ((noinline))
int looptarget() {
    int sum = 0;
    for (int iter = 2; iter < ITERS; iter += 1) { // Start from 2, go up to ITERS
        int isPrime = 1; // Assume the number is prime
        for (int j = 2; j * j <= iter; j++) {
            if (iter % j == 0) {
                isPrime = 0; // Number is not prime
                break;
            }
        }
        if (isPrime) {
            sum += iter;
        }
    }
    return sum;
}

int main(int argc, char* argv[]) {
   int t=looptarget();
   printf("Result %d",t);
}
