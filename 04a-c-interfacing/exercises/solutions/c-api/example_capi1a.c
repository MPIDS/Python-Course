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

  PyRun_SimpleString( "li = []\n"
							 "li.insert(0,2)\n"
							 "li.append(10)\n"
							 "print li\n");

  Py_Finalize();

  return 0;
}
