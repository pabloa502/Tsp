default : nearest_neighbor

.PHONY : install
install :
	apt-get install -y python-dev
	pip install numpy
	pip install matplotlib

.PHONY : nearest_neighbor
nearest_neighbor :
	python Tsp.py

.PHONY : pilot
pilot :
	python TspPilot.py
