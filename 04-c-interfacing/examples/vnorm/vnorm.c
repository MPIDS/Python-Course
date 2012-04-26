#include <math.h>

double vnorm( double *vec, int lvec ){
  double r=0.0;
  int i;
  for( i=0; i<lvec; i++ )
	 r+=vec[i]*vec[i];
  return sqrt(r);
}
