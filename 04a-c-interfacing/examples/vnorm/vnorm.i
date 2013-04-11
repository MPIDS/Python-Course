%module vnorm
%{
#define SWIG_FILE_WITH_INIT
double vnorm( double *vec, int lvec );
%}

%include "numpy.i"

%init %{
import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* vec, int lvec)};
double vnorm( double *vec, int lvec );


