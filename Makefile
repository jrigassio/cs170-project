pycosat.so: libpicosat.a pycosat.c
	python setup.py build_ext --inplace

picosat.o: picosat.c picosat.h
	$(CC) $(CFLAGS) -fPIC -c $<

libpicosat.a: picosat.o
	ar rc $@ picosat.o


test: pycosat.so
	python  test_pycosat.py

clean:
	rm -rf build dist *.egg-info
	rm -f *.pyc *.so *.o *.a
