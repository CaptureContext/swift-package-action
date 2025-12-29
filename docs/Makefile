github-build-docs:
	@echo "Running github-build-docs for $(SCHEME)"
	@chmod +x '.scripts/github-build-docs'
	SCHEME=$(SCHEME) ./.scripts/github-build-docs

PLATFORM_IOS = iOS Simulator,id=$(call udid_for,iOS,iPhone \d\+ Pro [^M])
PLATFORM_MACOS = macOS
PLATFORM_MAC_CATALYST = macOS,variant=Mac Catalyst
PLATFORM_TVOS = tvOS Simulator,id=$(call udid_for,tvOS,TV)
PLATFORM_VISIONOS = visionOS Simulator,id=$(call udid_for,visionOS,Vision)
PLATFORM_WATCHOS = watchOS Simulator,id=$(call udid_for,watchOS,Watch)

ifeq ($(PLATFORM),iOS)
	DESTINATION = "$(PLATFORM_IOS)"
else ifeq ($(PLATFORM),macOS)
	DESTINATION = "$(PLATFORM_MACOS)"
else ifeq ($(PLATFORM),tvOS)
	DESTINATION = "$(PLATFORM_TVOS)"
else ifeq ($(PLATFORM),watchOS)
	DESTINATION = "$(PLATFORM_WATCHOS)"
else ifeq ($(PLATFORM),visionOS)
	DESTINATION = "$(PLATFORM_VISIONOS)"
else ifeq ($(PLATFORM),macCatalyst)
	DESTINATION = "$(PLATFORM_MAC_CATALYST)"
else
	DESTINATION = __unsupported__
endif

DOC_WARNINGS = $(shell \
	xcodebuild clean docbuild \
		-scheme "$(SCHEME)" \
		-destination platform="$(DESTINATION)" \
		-quiet 2>&1 \
		| grep "couldn't be resolved to known documentation" \
		| sed 's|$(PWD)|.|g' \
		| tr '\n' '\1' \
)

test-docs:
	@echo "Running test-docs for $(SCHEME) [$(PLATFORM)]"
	@test "$(DOC_WARNINGS)" = "" \
		|| (echo "xcodebuild docbuild failed:\n\n$(DOC_WARNINGS)" | tr '\1' '\n' \
		&& exit 1)

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
