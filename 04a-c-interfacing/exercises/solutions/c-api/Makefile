PYVER=2.7

all: example_capi1a example_capi1b mycalculator


example_capi1a: example_capi1a.c
	gcc -I /usr/include/python$(PYVER)/ example_capi1a.c -o example_capi1a -lpython$(PYVER)

example_capi1b: example_capi1b.c
	gcc -I /usr/include/python$(PYVER)/ example_capi1b.c -o example_capi1b -lpython$(PYVER)

mycalculator: mycalculator.c
	gcc -I /usr/include/python$(PYVER)/ mycalculator.c -o mycalculator -lpython$(PYVER)
