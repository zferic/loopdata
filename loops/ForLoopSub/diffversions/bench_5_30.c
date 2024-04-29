#include <stdio.h>

#define STEP   5
#define ITERS   30

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 100000;
  for(iter=0; iter < ITERS; ++iter) {
    sum-=STEP;
  }
  return sum;
}

int main(int argc, char* argv[]) {

   int t=looptarget();
   printf("Result %d",t);

}
