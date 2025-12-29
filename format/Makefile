ifeq ($(MAKECMDGOALS),swift-format)
	ifeq (FORMATTER_CONFIG, __unspecified__)
		SWIFT_FORMAT_FLAGS = \
			--ignore-unparsable-files \
			--in-place
	else
		SWIFT_FORMAT_FLAGS = \
			--configuration $(FORMATTER_CONFIG) \
			--ignore-unparsable-files \
			--in-place
	endif

	SWIFT_FORMAT_COMMAND = swift format $(SWIFT_FORMAT_FLAGS)
endif

swift-format:
	@echo "Running swift-format"
	@make _runpy FORMATTER=swift-format

venv:
	@rm -rf .venv
	@python3 -m venv .venv

_runpy:
	@chmod +x $(CURDIR)/.venv/bin/activate && $(CURDIR)/.venv/bin/activate
	@chmod +x "$(CURDIR)/.venv/bin/python" && "$(CURDIR)/.venv/bin/python" __init__.py

# test action to validate if makefile is correct
ping:
	@echo "pong 🏓"
