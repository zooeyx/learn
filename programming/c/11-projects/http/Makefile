# Build all lesson subdirectories
LESSONS = $(sort $(wildcard */))

.PHONY: all clean $(LESSONS)

all: $(LESSONS)

$(LESSONS):
	@if [ -f $@Makefile ]; then $(MAKE) -C $@; fi

clean:
	@for l in $(LESSONS); do \
		if [ -f $$l/Makefile ]; then $(MAKE) -C $$l clean; fi; \
	done
