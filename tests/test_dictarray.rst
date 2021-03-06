>>> import numpy
>>> from cogent import DNA
>>> from cogent.util.dict_array import DictArrayTemplate
>>> a = numpy.identity(3, int)
>>> b = DictArrayTemplate('abc', 'ABC').wrap(a)
>>> b[0]
===========
A    B    C
-----------
1    0    0
-----------
>>> b['a']
===========
A    B    C
-----------
1    0    0
-----------
>>> b.keys()
['a', 'b', 'c']
>>> row = b['a']
>>> row.keys()
['A', 'B', 'C']
>>> list(row)
[1, 0, 0]
>>> sum(row)
1
>>> # Dimensions can also be ordinay integers
>>> b = DictArrayTemplate(3, 3).wrap(a)
>>> b.keys()
[0, 1, 2]
>>> b[0].keys()
[0, 1, 2]
>>> sum(b[0])
1
>>> # Or a mix
>>> b = DictArrayTemplate('ABC', 3).wrap(a)
>>> b.keys()
['A', 'B', 'C']
>>> b['A'].keys()
[0, 1, 2]

``DictArray`` should work properly in ``numpy`` operations.

>>> darr = DictArrayTemplate(list(DNA), list(DNA)).wrap([[.7,.1,.1,.1],
...                                                      [.1,.7,.1,.1],
...                                                      [.1,.1,.7,.1],
...                                                      [.1,.1,.1,.7]])
>>> mprobs = numpy.array([0.25, 0.25, 0.25, 0.25])
>>> print mprobs.dot(darr)
[ 0.25  0.25  0.25  0.25]
>>> print numpy.dot(mprobs, darr)
[ 0.25  0.25  0.25  0.25]
