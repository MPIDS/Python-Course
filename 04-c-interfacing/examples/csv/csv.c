#include<stdio.h>
#include<stdlib.h>

int main(){
  FILE *f=fopen("test.csv","r");
  float *values;
  int i, c, n=1;

  while( (c=fgetc(f))!=EOF )
	 if( c==',' ) n++;
  rewind(f);

  values =(float*)malloc(n*sizeof(float));

  for( i=0; i<n; i++ )
	 fscanf( f, "%f,", &(values[i]) );

  for( i=0; i<n; i++ )
	 fprintf( stdout, "%f, ", values[i] );

  fclose(f);
  free(values);
}
