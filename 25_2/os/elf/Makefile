CC := gcc
CFLAGS := -Wall -Wextra -O0 -g -fno-pie -no-pie
TARGET := hello_elf
.PHONY: all run inspect clean
all: $(TARGET)
$(TARGET): hello_elf.c
	$(CC) $(CFLAGS) -o $@ $<
run: $(TARGET)
	./$(TARGET)
inspect: $(TARGET)
	./inspect_elf.sh ./$(TARGET)
clean:
	rm -f $(TARGET)
