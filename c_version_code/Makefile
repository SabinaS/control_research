CC=gcc
CFLAGS=-I.
DEPS = bang_bang_controller.h


%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

bang_bang_controller: bang_bang_controller.o 
	gcc -o bang_bang_controller bang_bang_controller.o -I.
     
.PHONY: clean

clean:
	rm -f *.o *~ 
