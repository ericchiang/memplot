memplot
=======

Plot the memory usage of arbitrary processes


Install
-------

pypi:
```bash
$ pip install memplot
```

From source:
```bash
$ git clone https://github.com/EricChiang/memplot.git
$ cd memplot
$ python setup.py install
```

Usage
-----

What's the memory usage of the `pickle` package? Let's consider the following script save under `pickle_array.py`
```python
import numpy as np
import pickle
import time

x = np.random.randn(1000,10000)
time.sleep(1)
pickle.dump(x,open("x.pk","w"))
```

To plot memory usage run:
```bash
$ memplot "python pickle_array.py"
```

This command produces the following plot:
![pickle an array](imgs/python_pickle_array.png)

How does R do? Here's a similar serialization script saved as `save_array.r`

```Rscript
x <- matrix(rnorm(1000,10000),1000,10000)
Sys.sleep(1)
save(x,file="x.Rdata")
```

Time to plot the memory usage:
```bash
$ memplot "Rscript save_array.r"
```

![save an array](imgs/r_save_array.png)
