%module cft
%{
    #define SWIG_FILE_WITH_INIT
    #include "cosft_py.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* INPLACE_ARRAY1, int DIM1) {(double* data, int n)}

%include "cosft_py.h"
%clear (double* data, int n);
