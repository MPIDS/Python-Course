#include "Python.h"
#include <stdio.h>

int main( int argc, char **argv ){
  char buf[1000];

  Py_Initialize();

  PyRun_SimpleString( "from math import *");

  sprintf( buf, "cmd='%s'", argv[1]);
  PyRun_SimpleString( buf );
  sprintf( buf, "result=(%s)", argv[1]);
  PyRun_SimpleString( buf );
  
  PyRun_SimpleString( "print 'Result of ',cmd,'=', result");

  Py_Finalize();

  return 0;
}
