#include <stdio.h>

#define STEP   5
#define ITERS   7

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 0;
      for(int iter = 0; iter < ITERS; ++iter) {
          for(int j = 0; j < STEP; ++j) {
              sum += STEP;
          }
      }
      return sum;
}

int main(int argc, char* argv[]) {
   int t=looptarget();
   printf("Result %d",t);
}
