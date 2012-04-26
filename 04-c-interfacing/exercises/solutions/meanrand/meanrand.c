#include <stdlib.h>
#include <time.h>
#include "meanrand.h"

unsigned int seed=0;

void setseed( unsigned int myseed ){
  srandom( myseed );
  seed=myseed;
}

float meanrand2( long n, float a, float b ){
  float res=0.0;

  if( seed==0 ){
	 seed=(unsigned int)time(NULL);
	 setseed( seed );
  }
  
  long i;
  for( i=0; i<n; i++ ){
	 res += (a+((float)(random())/RAND_MAX)*(b-a));
  }
  res = res/(float)n;
  
  return res;
}


float meanrand( long n ){
  return meanrand2( n, 0.0, 1.0 );
}


