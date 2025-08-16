include makefile_utils/defaults.mk

PYTHON = python3

.PHONY: test clean update setup

test:
	@ . ./$(VENV_ACTIVATE) && python -m pytest -v
	@ echo "all tests passed"

clean: python-clean

update: git-submodule-update venv-force-install-deps

setup: git-hook-install venv-setup

include makefile_utils/git.mk
include makefile_utils/python.mk
include makefile_utils/venv.mk
