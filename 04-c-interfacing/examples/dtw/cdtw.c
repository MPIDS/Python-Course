#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define matIDX( m, n1, i1, i2 )						\
  *((m+(i2*n1))+i1)

#define pIDX( p, np, i1, i2 )							\
  *(p+(np*i2)+i1)

double min3( double m1, double m2, double m3 ){
  if( m1<m2 ){
	 if( m1<m3 )
		return m1;
	 else 
		return m3;
  } else if (m2<m3)
	 return m2;
  else return m3;
}

/** calculate shortest path through matrix M.
	 \param M is a n1 x n2 matrix
	 \param p is the path, a nd x np matrix of corresponding matrix indices,
              nd=2 (else the typemaps do not work properly)
	 \return 0 in case of success, 1 otherwise
 */
int cdtw( double *M, int n1, int n2, int *p, int nd, int np ){
  int i,j;
  /* argument checks */
  if( nd!=2 ){
	 printf("nd needs to be 2, found %i\n", nd);
	 return 1;
  }
  if( np<n1+n2 ){
	 printf("path may be too short, %i<%i\n", np, n1+n2);
	 return 1;
  }

  double *D=(double*)malloc( n1*n2*sizeof(double));
  memcpy( D, M, n1*n2*sizeof(double));
  for( i=0; i<n1; i++ )
	 for( j=0; j<n2; j++ )
		matIDX(D,n1,i+1,j+1)=
		  matIDX(M,n1,i,j)+min3(matIDX(D,n1,i,j+1),
										matIDX(D,n1,i+1,j),
										matIDX(D,n1,i+1,j+1));
  
  i=n1-1;
  j=n2-1;

  pIDX( p, np, 0, 0 ) = i;
  pIDX( p, np, 0, 1 ) = j;
  int pi=1;
  while( i>0 || j>0 ){
	 if( i>0 && j>0 ){
		if( matIDX(D,n1,i,j-1)<matIDX(D,n1,i-1,j-1) ){
		  if( matIDX(D,n1,i,j-1)<matIDX(D,n1,i-1,j) ){
			 j--;
		  } else {
			 i--;
		  }
		} else {
		  if( matIDX(D,n1,i-1,j-1)<matIDX(D,n1,i-1,j)  ){
			 i--; j--;
		  } else {
			 j--;
		  }
		}
	 } else if( i>0 ){ // i>0, j==0
		i--;
	 } else { // i==0, j>0
		j--;
	 }

	 pIDX( p, np, pi, 0) = i;
	 pIDX( p, np, pi, 1) = j;
	 pi++;
  }
  
  free( D );
  return 0;
}

