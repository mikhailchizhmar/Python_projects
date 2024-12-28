all: install

install:
#	sudo apt-get install python3-tk
	python3 Part3/MazeSolverGUI.py
	python3 Part4/CaveGUI.py

tests:
	python3 Part2/unittests.py
	python3 Part3/unittests.py
	python3 Part4/unittests.py
	python3 Part5/unittests.py

uninstall: clean

dvi:
	cat doc.txt

dist:
	tar -czf maze.tar.gz Part3
	tar -czf cave.tar.gz Part4

clean:
	rm -rf Part1/__pycache__ Part1/.pytest_cache
	rm -rf Part2/__pycache__ Part2/.pytest_cache
	rm -rf Part3/__pycache__ Part3/.pytest_cache
	rm -rf Part4/__pycache__ Part4/.pytest_cache
	rm -rf Part5/__pycache__ Part5/.pytest_cache
	rm -rf Part6/__pycache__ Part6/.pytest_cache
	rm -rf output_cave.txt test_cave.txt *.tar.gz
