%module geomean
%{
#define SWIG_FILE_WITH_INIT
#include "geomean.h"
%}


%include "numpy.i"

%init %{
import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double *x, int n)};
double geomean_pow( double *x, int n );
double geomean_ln( double *x, int n );

%pythoncode %{
%}
