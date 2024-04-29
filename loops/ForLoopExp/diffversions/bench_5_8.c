#include <stdio.h>

#define STEP   5
#define ITERS   8

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 0;
  for(int iter = 0; iter < ITERS; ++iter) {
      sum += STEP * (1 << iter); // Exponentially increase the addition
  }
  return sum;
}

int main(int argc, char* argv[]) {

   int t=looptarget();
   printf("Result %d",t);

}
