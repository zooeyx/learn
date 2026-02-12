# Build all project subdirectories
PROJECTS = $(wildcard */)

.PHONY: all clean $(PROJECTS)

all: $(PROJECTS)

$(PROJECTS):
	@if [ -f $@Makefile ]; then $(MAKE) -C $@; fi

clean:
	@for p in $(PROJECTS); do \
		if [ -f $$p/Makefile ]; then $(MAKE) -C $$p clean; fi; \
	done
