# common.mk — shared build rules for C chapters
# Include from chapter Makefiles: include ../common/common.mk

CC       = clang
CSTD     = -std=c17
WARNINGS = -Wall -Wextra -Wpedantic
DEBUG    = -g
CFLAGS   = $(CSTD) $(WARNINGS) $(DEBUG)

ifdef ASAN
CFLAGS  += -fsanitize=address -fno-omit-frame-pointer
LDFLAGS += -fsanitize=address
endif

BUILDDIR = build
SRCS     = $(wildcard *.c)
BINS     = $(patsubst %.c,$(BUILDDIR)/%,$(SRCS))

.PHONY: all clean run

all: $(BINS)

$(BUILDDIR)/%: %.c | $(BUILDDIR)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)

run: all
	@for bin in $(BINS); do \
		echo "\n=== $$(basename $$bin) ==="; \
		./$$bin; \
	done
