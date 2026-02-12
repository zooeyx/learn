# Top-level Makefile — delegates to language/topic directories
TOPICS = programming/c

.PHONY: all clean $(TOPICS)

all: $(TOPICS)

$(TOPICS):
	$(MAKE) -C $@

clean:
	@for t in $(TOPICS); do $(MAKE) -C $$t clean; done
