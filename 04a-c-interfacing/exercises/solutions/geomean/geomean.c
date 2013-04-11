#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "geomean.h"

double geomean_pow( double *x, int n ){
  int i;
  double gm;
  for( i=0; i<n; i++ ){
	 gm *= x[i];
  }
  gm=pow(gm, 1.0/n);
  return gm;
}

double geomean_ln( double *x, int n ){
  int i;
  double gm;
  for( i=0; i<n; i++ ){
	 gm += log(x[i]);
  }
  gm/=(double)n;
  gm=exp(gm);
  return gm;
}
