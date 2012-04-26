/*
gcc -fpic -c -I/usr/include/python2.7 primewrap.c -o primetest.o
gcc -shared primetest.o -o primetestmodule.so

*/
#include <Python.h>

int isprime( long num ){
  long i=2;
  while( i<num ){
	 if( num%i++==0 ) return 0;
  }
  return 1;
}


PyObject *wrap_isprime(PyObject *self, PyObject *args) {
  long num;
  if (!PyArg_ParseTuple(args,"l",&num))
	 return NULL;
  return isprime(num) ? Py_True : Py_False;

}

static PyMethodDef primeMethods[] = {
  { "isprime", wrap_isprime, 1 },
  { NULL, NULL }
};


void initprimetest() {
  PyObject *m;
  m = Py_InitModule("primetest", primeMethods);
}

