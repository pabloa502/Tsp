default : nearest_neighbor

.PHONY : install
install :
	pip install python-tk
	pip install numpy
	pip install matplotlib

.PHONY : nearest_neighbor
nearest_neighbor :
	python Tsp.py

.PHONY : pilot
pilot :
	python TspPilot.py
