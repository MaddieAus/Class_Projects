CC = gcc
CFLAGS = -g -Wall -std=c99 -pedantic
OBJS = main.o unity.o tests.o code.o
TARGET = main.exe

.PHONY: all clean

# ===== Default build (with source code) =====
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

main.o: main.c code.h tests.h unity.h
	$(CC) $(CFLAGS) -c main.c -o main.o

tests.o: tests.c tests.h code.h unity.h
	$(CC) $(CFLAGS) -c tests.c -o tests.o

unity.o: unity.c unity.h
	$(CC) $(CFLAGS) -c unity.c -o unity.o

code.o: code.c code.h
	$(CC) $(CFLAGS) -c code.c -o code.o

# ===== Student build (with precompiled code.o) =====
student: main.o tests.o unity.o code.o
	$(CC) main.o tests.o unity.o code.o -o $(TARGET)

# Note: here code.o is assumed to be precompiled and distributed

clean:
	del /f *.o $(TARGET)
