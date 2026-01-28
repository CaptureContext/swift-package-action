format:
	@echo "Running ${FORMATTER}"
	@make _runpy FORMATTER=${FORMATTER} CONFIG=$(CONFIG)

venv:
	@rm -rf .venv
	@python3 -m venv .venv

_runpy:
	@chmod +x $(CURDIR)/.venv/bin/activate && $(CURDIR)/.venv/bin/activate
	@chmod +x "$(CURDIR)/.venv/bin/python" && "$(CURDIR)/.venv/bin/python" __init__.py

# test action to validate if makefile is correct
ping:
	@echo "pong 🏓"
