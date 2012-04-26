#ifndef MEANRAND_H
#define MEANRAND_H


extern unsigned int seed;

void setseed( unsigned int myseed );
float meanrand( long n);
float meanrand2( long n, float a, float b );

#endif
