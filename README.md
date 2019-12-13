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
```
