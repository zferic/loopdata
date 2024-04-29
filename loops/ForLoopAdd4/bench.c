#include <stdio.h>
#define STEP   5
#define ITERS   32

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 0;
  for(iter = 0; iter < ITERS; ++iter) {
    sum += STEP;
    sum += iter;  // Add the current iteration count to sum
  }
  return sum;
}


int main(int argc, char* argv[]) {
   int t=looptarget();
   printf("Result %d",t);
}
