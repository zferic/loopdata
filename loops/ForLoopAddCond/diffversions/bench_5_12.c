#include <stdio.h>

#define STEP   5
#define ITERS   12

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 0;
  for(iter=0; iter < ITERS; ++iter) {
    if (sum < 50) {
      sum+=STEP;
    }
    if (sum > 50) {
      sum+=2*STEP;
    }
  }
  return sum;
}

int main(int argc, char* argv[]) {
   int t=looptarget();
   printf("Result %d",t);
}
