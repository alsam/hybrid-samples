# hybrid-samples
Hybrid Python/C++ packages, other languages

```sh
sudo pip3 install wheel
```

```python
python3
>>> v = [1.,2.,3.,]
>>> v1 = [6., -2., 2.]
>>> import vossen
>>> vossen.cosfft1(v, 2)
BEG: data[0] : 1
BEG: data[1] : 2
BEG: data[2] : 3
END: data[0] : 6
END: data[1] : -2
END: data[2] : 2
>>> vossen.cosfft1(v1, 2, inverse = True)
BEG: data[0] : 6
BEG: data[1] : -2
BEG: data[2] : 2
END: data[0] : 1
END: data[1] : 2
END: data[2] : 3
>>> 
```
