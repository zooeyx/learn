# Multi-file HTTP server Makefile
CC       = clang
CFLAGS   = -std=c17 -Wall -Wextra -Wpedantic -g
BUILDDIR = build
TARGET   = $(BUILDDIR)/server

ifdef ASAN
CFLAGS  += -fsanitize=address -fno-omit-frame-pointer
LDFLAGS += -fsanitize=address
endif

SRCS = $(wildcard *.c)
OBJS = $(patsubst %.c,$(BUILDDIR)/%.o,$(SRCS))

.PHONY: all clean run

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

$(BUILDDIR)/%.o: %.c | $(BUILDDIR)
	$(CC) $(CFLAGS) -c -o $@ $<

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)

run: all
	./$(TARGET) 8080 ../www
