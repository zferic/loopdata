#include <stdio.h>

#define STEP   5
#define ITERS   15

__attribute__ ((noinline))
int looptarget() {
  int iter;
  int sum = 0;
  for(iter=1; iter < ITERS; iter *= 2) {
    sum+=STEP;
    
  }
  return sum;
}

int main(int argc, char* argv[]) {

   int t=looptarget();
   printf("Result %d",t);

}
