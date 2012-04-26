%module meanrand
%{
#include "meanrand.h"
%}

float meanrand( long n);
float meanrand2( long n, float a, float b );
void  setseed( unsigned int seed );

/* Rewrite the high level interface to meanrand */
%pythoncode %{
def meanrand3( n=1000, a=0.0, b=1.0):
  return _meanrand.meanrand2(n, a,b)
%}
