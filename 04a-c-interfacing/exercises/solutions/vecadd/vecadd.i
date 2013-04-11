%module vecadd
%{
#define SWIG_FILE_WITH_INIT
#include "vecadd.h"
%}


%include "numpy.i"

%init %{
import_array();
%}

%apply (float* IN_ARRAY1, int DIM1) {(float *v1, int n1)};
%apply (float* IN_ARRAY1, int DIM1) {(float *v2, int n2)};
%apply (float* INPLACE_ARRAY1, int DIM1) {(float *out, int n3)};
int vecadd2(  float *v1, int n1, float *v2, int n2, float *out, int n3 );


%pythoncode %{
import numpy as np
def vecadd(v1,v2):
  n1,n2=len(v1),len(v2)
  if n1!=n2:
     raise RuntimeError("Lengths of v1 and v2 don't match, %i!=%i"%(n1,n2))
  if v1.dtype!=np.float32 or v2.dtype!=np.float32:
     raise TypeError("v1 or v2 of wrong type")
  v3=np.zeros(n1,dtype=np.float32)
  _vecadd.vecadd2( v1, v2, v3 )
  return v3

%}
