#include "vecadd.h"

int vecadd( float *v1, float *v2, int n, float *out ){
  int i;
  for( i=0; i<n; i++ ){
	 out[i]=v1[i]+v2[i];
  }
  return 0;
}

int vecadd2(  float *v1, int n1, float *v2, int n2, float *out, int n3 ){
  if( n1!=n2 || n1!=n3 )
	 return 1;

  return vecadd( v1, v2, n1, out );
}
