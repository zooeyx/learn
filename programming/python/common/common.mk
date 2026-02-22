# common.mk — shared build rules for Python chapters
# Include from chapter Makefiles: include ../common/common.mk

PYTHON = python3
SRCS   = $(filter-out __init__.py,$(wildcard *.py))

.PHONY: all run test lint clean

all: run

run:
	@for src in $(SRCS); do \
		echo "\n=== $$(basename $$src .py) ==="; \
		$(PYTHON) $$src; \
	done

test:
	@if [ -d tests ]; then $(PYTHON) -m pytest tests/ -v; else echo "No tests/"; fi

lint:
	@$(PYTHON) -m py_compile $(SRCS) && echo "All files compile OK"

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
	@find . -name '*.pyc' -delete 2>/dev/null; true
