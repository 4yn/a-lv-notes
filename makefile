# LaTeX Makefile
SHELL := /bin/bash
SUBDIRS := $(wildcard */.)
cleanregex = ".+\(aux\|log\|synctex.gz\|fls\|fdb_latexmk\|bbl\|blg\)$$"
cleanallregex = ".+\(aux\|log\|synctex.gz\|fls\|fdb_latexmk\|bbl\|blg\|pdf\)$$"

.PHONY: $(SUBDIRS) clean clean-p

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) contents -C $@
	$(MAKE) -C $@

clean:
	find -regex $(cleanregex) -delete

clean-a:
	find -regex $(cleanallregex) -delete

ac: clean-a all clean