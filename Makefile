default:
	$(error Missing command)
	@exit 1

%:
	$(error Unknown command: $@)
	@exit 1

PLATFORM_IOS ?= iOS Simulator,id=$(call udid_for,iOS,iPhone \d\+ Pro [^M])
PLATFORM_MACOS ?= macOS
PLATFORM_MAC_CATALYST ?= macOS,variant=Mac Catalyst
PLATFORM_TVOS ?= tvOS Simulator,id=$(call udid_for,tvOS,TV)
PLATFORM_VISIONOS ?= visionOS Simulator,id=$(call udid_for,visionOS,Vision)
PLATFORM_WATCHOS ?= watchOS Simulator,id=$(call udid_for,watchOS,Watch)
DERIVED_DATA ?= "~/.derivedData"

GREEN=\033[0;32m
RED=\033[0;31m
BOLD=\033[1m
RESET=\033[0m

RESOLVED_PLATFORM ?= $(call resolve_platform,$(PLATFORM))
PLATFORMS ?= "$(PLATFORM)"

loop-platforms:
	@$(eval MAKEFILE_PATH ?= "./Makefile")
	@$(eval platforms := $(shell echo $(PLATFORMS) | sed 's/,/ /g'))
	@$(foreach platform,$(platforms),$(MAKE) -f $(MAKEFILE_PATH) $(GOAL) PLATFORM=$(platform);)

xcodebuild:
	$(call run_xcodebuild,$(SCHEME))

xcodebuild-macros:
	$(call run_xcodebuild,$(SCHEME)Macros)

xcodebuild-macros-plugin:
	$(call run_xcodebuild,$(SCHEME)MacrosPlugin)

build-for-library-evolution:
	@swift build \
		-c release \
		--target "$(SCHEME)" \
		-Xswiftc -emit-module-interface \
		-Xswiftc -enable-library-evolution

#workaround for instant echo output
test-docs-start:
	@echo "$(BOLD)Testing$(RESET) Documentation"
	
test-docs: test-docs-start
	$(shell \
		export DOC_WARNINGS = xcodebuild clean docbuild \
			-scheme "$(SCHEME)" \
			-destination platform="$(RESOLVED_PLATFORM)" \
			-quiet 2>&1 \
			| grep "couldn't be resolved to known documentation" \
			| sed 's|$(PWD)|.|g' \
			| tr '\n' '\1' \
	)
	@test "$(DOC_WARNINGS)" = "" \
		|| (echo "$(BOLD)$(RED)xcodebuild docbuild failed:$(RESET)\n\n$(DOC_WARNINGS)" | tr '\1' '\n' \
		&& exit 1)
	@echo "$(GREEN)$(BOLD)Documentation tests succeeded$(RESET)"

test-example:
	@xcodebuild test \
		-skipMacroValidation \
		-scheme "$(SCHEME)" \
		-destination platform="$(RESOLVED_PLATFORM)" \
		-derivedDataPath $(DERIVED_DATA)

test-integration:
	@xcodebuild test \
		-skipMacroValidation \
		-scheme "$(SCHEME)" \
		-destination platform="$(RESOLVED_PLATFORM)"

benchmark:
	@swift run --configuration release \
		swift-composable-architecture-benchmark

format:
	@find . \
		-path '*/Documentation.docc' -prune -o \
		-name '*.swift' \
		-not -path '*/.*' -print0 \
		| xargs -0 swift format --ignore-unparsable-files --in-place

define run_xcodebuild
	@$(eval BASE_SCHEME := $(1))
	@$(eval TEST_SCHEME := $(1)Tests)
	@$(eval CURRENT_SCHEME = $(if $(filter $(COMMAND),test),$(TEST_SCHEME),$(BASE_SCHEME)))
	@$(eval CURRENT_PLATFORM := $(RESOLVED_PLATFORM))
	@$(if $(filter $(CURRENT_PLATFORM), Unsupported), $(error Unsupported platform: $(PLATFORM)))

	@$(eval FORMATTED_COMMAND = $(if $(filter $(COMMAND),test),xcodebuild (test),xcodebuild))
	@echo "\n$(BOLD)$(FORMATTED_COMMAND)$(RESET)"
	@echo "$(BOLD)Scheme:$(RESET) $(CURRENT_SCHEME) ($(CONFIG))"
	@echo "$(BOLD)Platform:$(RESET) $(CURRENT_PLATFORM)\n"
	
	xcodebuild \
		-skipMacroValidation \
		-configuration $(CONFIG) \
		-workspace .github/package.xcworkspace \
		-scheme $(CURRENT_SCHEME) \
		-destination platform="$(CURRENT_PLATFORM)" \
		-derivedDataPath "$(DERIVED_DATA)/$(CONFIG)" \
		$(COMMAND) | xcpretty || exit 1
endef

define resolve_platform
	$(shell \
		if [ "$(1)" = "iOS" ]; then \
			echo $(PLATFORM_IOS); \
		elif [ "$(1)" = "macOS" ]; then \
			echo $(PLATFORM_MACOS); \
		elif [ "$(1)" = "macCatalyst" ]; then \
			echo $(PLATFORM_MAC_CATALYST); \
		elif [ "$(1)" = "watchOS" ]; then \
			echo $(PLATFORM_WATCHOS); \
		elif [ "$(1)" = "tvOS" ]; then \
			echo $(PLATFORM_TVOS); \
		elif [ "$(1)" = "visionOS" ]; then \
			echo $(PLATFORM_VISIONOS); \
		else \
			echo "Unsupported"; \
		fi \
	)
endef

define udid_for
$(shell \
	xcrun simctl list devices available '$(1)' \
	| grep '$(2)' \
	| sort -r \
	| head -1 \
	| awk -F '[()]' '{ print $$(NF-3) }' \
)
endef
