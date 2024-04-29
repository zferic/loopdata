#include <stdio.h>

#define STEP   5
#define ITERS   15

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 1;
  for(iter=0; iter < ITERS; ++iter) {

    sum=sum + sum*ITERS;

  }
  return sum;
}

int main(int argc, char* argv[]) {

   int t=looptarget();
   printf("Result %d",t);

}
