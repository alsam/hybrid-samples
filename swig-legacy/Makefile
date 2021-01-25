all:
	swig -python cft.i
	gcc -fPIC -c cft.c cft_wrap.c cosft_py.c -I /usr/include/python3.9 -I /usr/lib/python3.9/site-packages/numpy/core/include
	gcc -shared cft.o cft_wrap.o cosft_py.o -o _cft.so
	python3 -c "import cft; import numpy as np; x = np.array([1.,2,3]); cft.cosft(x); print(x); cft.icosft(x); print(x)"
