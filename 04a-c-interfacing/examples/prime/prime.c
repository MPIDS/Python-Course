#include<stdio.h>

int isprime( long num ){
  long i=2;
  while( i<num ){
	 if( num%i++==0 ) return 0;
  }
  return 1;
}

int main(){
  printf( "%d\n", isprime(715827883) );
}
