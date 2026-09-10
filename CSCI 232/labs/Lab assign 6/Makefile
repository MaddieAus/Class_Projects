
CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -lm

# Source files
SRC = code.c test_code.c unity.c
OBJ = $(SRC:.c=.o)
TARGET = test_runner

# Default target: build and run tests
all: $(TARGET)
	./$(TARGET)

# Link object files
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(CFLAGS)

# Compile each .c file into .o
%.o: %.c
	$(CC) -c $< -o $@ $(CFLAGS)

# Clean build files
clean:
	rm -f $(OBJ) $(TARGET)

# Run tests explicitly
test: all
