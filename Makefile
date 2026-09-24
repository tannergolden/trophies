# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
#
# The kit is stdlib-only Python, so every target below runs on a bare
# `python3` with nothing installed.

PYTHON ?= python3
KIT    := $(PYTHON) src/trophy-kit.py

.DEFAULT_GOAL := help
.PHONY: help preview preview-repository preview-crest catalogue check self-test test clean-preview

## help: List the available targets
help:
	@echo "Trophies - the Trophy Kit"
	@echo
	@grep -E '^## ' $(MAKEFILE_LIST) | sed -e 's/## /  /' -e 's/:/\t-/' | column -t -s $$'\t'

## preview: Render the sample profile case into preview/ (no network)
preview:
	@mkdir -p preview/profile
	@$(KIT) preview --root preview/profile --mode profile --owner --today 2026-09-24

## preview-repository: Render the sample repository case into preview/ (no network)
preview-repository:
	@mkdir -p preview/repository
	@$(KIT) preview --root preview/repository --mode repository --today 2026-09-24

## preview-crest: The same sample in the crest style
preview-crest:
	@mkdir -p preview/crest
	@$(KIT) preview --root preview/crest --mode profile --style crest --today 2026-09-24

## catalogue: Regenerate docs/Catalogue.md from the data
catalogue:
	@$(KIT) catalogue > docs/Catalogue.md

## check: CI gate - self-test, the catalogue page is current, the sample renders and re-checks clean
check: self-test
	@$(KIT) catalogue | diff -q - docs/Catalogue.md >/dev/null || (echo "docs/Catalogue.md is stale: run make catalogue" && exit 1)
	@rm -rf preview/check && mkdir -p preview/check
	@$(KIT) preview --root preview/check --mode profile --today 2026-09-24 >/dev/null
	@$(KIT) check --root preview/check --mode profile --today 2026-09-24
	@rm -rf preview/check

## self-test: Renderer invariants and the golden hash (no repository needed)
self-test:
	@$(KIT) self-test

## test: Everything CI runs - the gate plus the unit tests
test: check
	@echo "Running the kit's tests..."
	@$(PYTHON) -m unittest discover -s tests -p 'test_*.py'
	@echo "Running repository script tests..."
	@$(PYTHON) -m unittest discover -s .github/scripts -p 'test_*.py'

## clean-preview: Remove rendered previews
clean-preview:
	@rm -rf preview
