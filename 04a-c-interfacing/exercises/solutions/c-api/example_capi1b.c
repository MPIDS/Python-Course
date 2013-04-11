/** implements the following python code:

li = []
li.insert(0,2)
li.append(10)
print li
*/

#include "Python.h"
#include <stdio.h>


int main(){
  Py_Initialize();

  PyObject *li=PyList_New(0);
  PyList_Insert( li, 0, PyInt_FromLong(2));
  PyList_Append( li, PyInt_FromLong(10));

  PyObject_Print( li, stdout, 0);

  Py_Finalize();

  return 0;
}
