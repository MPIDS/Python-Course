import scipy.weave as w
code="""
long i=2;
int r=1;
while( i<num ){
   if( num%i++==0 ) { r=0; break; }
}
return_val=r;
"""
num=715827883
print w.inline(code, ['num'])
