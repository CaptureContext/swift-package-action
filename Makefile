print-destination:
	@make print-destination -f $(ROOT_ACTION_PATH)/build/Makefile

warm-simulator:
	@make warm-simulator -f $(ROOT_ACTION_PATH)/build/Makefile

xcodebuild:
	@make xcodebuild -f $(ROOT_ACTION_PATH)/build/Makefile

xcodebuild-test:
	@make xcodebuild-test -f $(ROOT_ACTION_PATH)/build/Makefile

# Workaround for debugging Swift Testing tests: https://github.com/cpisciotta/xcbeautify/issues/313
xcodebuild-raw:
	@make xcodebuild-raw -f $(ROOT_ACTION_PATH)/build/Makefile

# Workaround for debugging Swift Testing tests: https://github.com/cpisciotta/xcbeautify/issues/313
xcodebuild-test-raw:
	@make xcodebuild-test-raw -f $(ROOT_ACTION_PATH)/build/Makefile

build-for-library-evolution:
	@make build-for-library-evolution -f $(ROOT_ACTION_PATH)/build/Makefile

benchmark:
	@make benchmark -f $(ROOT_ACTION_PATH)/build/Makefile

test-docs:
	@make test-docs -f $(ROOT_ACTION_PATH)/build/Makefile

github-build-docs:
	@echo "Running github-build-docs for $(SCHEME)"
	@chmod +x '.scripts/github-build-docs'
	SCHEME=$(SCHEME) ./.scripts/github-build-docs

format:
	@make _runpy module=format

venv:
	@rm -rf .venv
	@python3 -m venv .venv

_runpy:
	@chmod +x $(CURDIR)/.venv/bin/activate && $(CURDIR)/.venv/bin/activate
	@chmod +x "$(CURDIR)/.venv/bin/python" && "$(CURDIR)/.venv/bin/python" -m $(module)

.PHONY: build-for-library-evolution format warm-simulator xcodebuild xcodebuild-raw test-docs

define udid_for
$(shell \
	xcrun simctl list devices available '$(1)' \
	| grep '$(2)' \
	| sort -r \
	| head -1 \
	| awk -F '[()]' '{ print $$(NF-3) }' \
)
endef

# simple action for testing if Makefile is valid
ping:
	@echo "pong 🏓"
