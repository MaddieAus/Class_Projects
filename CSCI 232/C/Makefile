CC = gcc
CFLAGS = -g -Wall -std=c99 -pedantic
OBJS = main.o unity.o
TARGET = main.exe

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

main.o: main.c unity.h
	$(CC) $(CFLAGS) -c main.c -o main.o

unity.o: unity.c unity.h
	$(CC) $(CFLAGS) -c unity.c -o unity.o

clean:
	del /f *.o $(TARGET)  # Windows
