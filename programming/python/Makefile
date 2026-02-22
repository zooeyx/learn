# Recursive Makefile — runs all chapters
CHAPTERS = $(sort $(wildcard [0-9]*/))

.PHONY: all clean test $(CHAPTERS)

all: $(CHAPTERS)

$(CHAPTERS):
	$(MAKE) -C $@

test:
	@for ch in $(CHAPTERS); do echo "\n=== $$ch ==="; $(MAKE) -C $$ch test; done

clean:
	@for ch in $(CHAPTERS); do $(MAKE) -C $$ch clean; done
