# hybrid-samples
Hybrid Python/C++ packages, other languages

```sh
sudo pip3 install wheel
```

```python
python3
>>> import vossen
>>> v = vossen.VectorDouble([1.,2.,3.,])
>>> v
VectorDouble[1, 2, 3]
>>> vossen.cosfft1(v, 2)
>>> v
VectorDouble[6, -2, 2]
>>> vossen.cosfft1(v, 2, inverse = True)
>>> v
VectorDouble[1, 2, 3]
>>> import numpy as np
>>> x = np.array([1.,2.,3.,])
>>> x
array([1., 2., 3.])
>>> vossen.scale_by_2(x)
>>> x
array([2., 4., 6.])
```
