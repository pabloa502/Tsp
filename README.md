# Tsp

Camilo Andrés Rodríguez Garzón

This is an implementation of the TSP problem, this is solved with a couple of methods such as the nearest neighbor and the pilot method.


Requirements
------------
- [numpy](http://www.numpy.org/)
- [copy](https://docs.python.org/2/library/copy.html)
- [math](https://docs.python.org/2/library/math.html)
- [matplotlib](https://matplotlib.org/)

Install for linux
-------

```
   make install
```

### Testing

The module can test for

`Tsp Pilot with:`
```
   python TspPilot.py

   python TspPilot.py pr439.tsp 2 2 10
```
and

`Tsp Nearest Neighbors with:`
```
   python Tsp.py

   python Tsp.py pr439.tsp
```

Run
-------

You can run of basic example with:

```
   Make
   Make nearest_neighbor
   Make pilot
```
