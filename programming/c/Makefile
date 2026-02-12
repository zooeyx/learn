# Recursive Makefile — builds all chapters
CHAPTERS = $(sort $(wildcard [0-9]*/))

.PHONY: all clean $(CHAPTERS)

all: $(CHAPTERS)

$(CHAPTERS):
	$(MAKE) -C $@

clean:
	@for ch in $(CHAPTERS); do $(MAKE) -C $$ch clean; done
