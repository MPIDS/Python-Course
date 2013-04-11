%module cdtw
%{
#define SWIG_FILE_WITH_INIT
  int cdtw( double *M, int n1, int n2, int *p, int nd, int np );
%}

%include "numpy.i"

%init %{
import_array();
%}

%apply (double* IN_ARRAY2, int DIM1, int DIM2) {(double* M, int n1, int n2)};
%apply (int* INPLACE_ARRAY2, int DIM1, int DIM2) {(int* p, int nd, int np)};
int cdtw( double *M, int n1, int n2, int *p, int nd, int np );

/* Rewrite the high level interface to cdtw */
%pythoncode %{
import numpy as np
def cdtw(M):
  n1,n2=M.shape
  p=np.array(-1*np.ones( (2,2*n1), dtype=np.int32),dtype=np.int32)
  _cdtw.cdtw(M, p)
  p=np.row_stack( (p[0,:][(p[0,:]>=0)][::-1], p[1,:][(p[1,:]>=0)][::-1]))
					
  return p
%}
