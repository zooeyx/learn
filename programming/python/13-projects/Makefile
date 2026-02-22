# Projects — no common.mk, each project runs independently
PROJECTS = $(sort $(wildcard */))

.PHONY: all clean $(PROJECTS)

all:
	@echo "Projects available:"
	@for p in $(PROJECTS); do echo "  $$p"; done
	@echo "\nRun individually: cd <project> && python3 main.py"

$(PROJECTS):
	cd $@ && python3 main.py

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
