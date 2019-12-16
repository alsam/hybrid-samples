#include "cft.h"

void cosft(double *data, int n)  {cosfft1(data,n-1, 1);}
void icosft(double *data, int n) {cosfft1(data,n-1,-1);}

