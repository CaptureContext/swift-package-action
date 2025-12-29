MAKEFILE_DIR := "$(dir $(abspath $(firstword $(MAKEFILE_LIST))))"
MAKEFILE_PATH := "$(MAKEFILE_DIR)/Makefile"

print-destination:
	@echo "Running print-destination for $(PLATFORM)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=destination

warm-simulator:
	@echo "Running warm-simulator for $(PLATFORM)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=warm-simulator

xcodebuild:
	@-make warm-simulator -f $(ACTION_PATH)/build/Makefile
	@echo "Running xcodebuild)"
	@echo "  Workspace: $(WORKSPACE)"
	@echo "  Scheme: $(SCHEME)"
	@echo "  Config: $(CONFIG)"
	@echo "  Platform: $(PLATFORM)"
	@echo "  DerivedData: $(DERIVED_DATA_PATH)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=xcodebuild

xcodebuild-test:
	@-make warm-simulator -f $(ACTION_PATH)/build/Makefile
	@echo "Running xcodebuild-test"
	@echo "  Workspace: $(WORKSPACE)"
	@echo "  Scheme: $(SCHEME)"
	@echo "  Config: $(CONFIG)"
	@echo "  Platform: $(PLATFORM)"
	@echo "  DerivedData: $(DERIVED_DATA_PATH)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=xcodebuild-test

xcodebuild-raw:
	@-make warm-simulator -f $(ACTION_PATH)/build/Makefile
	@echo "Running xcodebuild-raw"
	@echo "  Workspace: $(WORKSPACE)"
	@echo "  Scheme: $(SCHEME)"
	@echo "  Config: $(CONFIG)"
	@echo "  Platform: $(PLATFORM)"
	@echo "  DerivedData: $(DERIVED_DATA_PATH)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=xcodebuild \
		BEAUTIFY=false

xcodebuild-test-raw:
	@-make warm-simulator -f $(ACTION_PATH)/build/Makefile
	@echo "Running xcodebuild-test-raw"
	@echo "  Workspace: $(WORKSPACE)"
	@echo "  Scheme: $(SCHEME)"
	@echo "  Config: $(CONFIG)"
	@echo "  Platform: $(PLATFORM)"
	@echo "  DerivedData: $(DERIVED_DATA_PATH)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=xcodebuild-test \
		BEAUTIFY=false

build-for-library-evolution:
	@echo "Running build-for-library-evolution for $(SCHEME)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=build-for-library-evolution

benchmark:
	@echo "Running benchmark for $(SCHEME)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=benchmark

test-docs:
	@echo "Running test-docs for $(SCHEME) $(PLATFORM)"
	@make _runpy \
		-f $(MAKEFILE_PATH) \
		COMMAND=test-docs

venv:
	@rm -rf .venv
	@python3 -m venv .venv

_runpy:
	@chmod +x $(CURDIR)/.venv/bin/activate && $(CURDIR)/.venv/bin/activate
	@chmod +x "$(CURDIR)/.venv/bin/python" && "$(CURDIR)/.venv/bin/python" "$(MAKEFILE_DIR)/__init__.py"

# test action to validate if makefile is correct
ping:
	@echo "pong 🏓"
