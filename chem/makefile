# LaTeX Makefile
SHELL := /bin/bash
FILE=main
cleanregex = ".+\(aux\|log\|synctex.gz\|fls\|fdb_latexmk\|bbl\|blg\)$$"
cleanpdfregex = ".+/content/.+\(pdf\)$$"
cleanallregex = ".+\(aux\|log\|synctex.gz\|fls\|fdb_latexmk\|bbl\|blg\|pdf\)$$"

.PHONY: clean clean-p $(FILE).pdf

$(FILE).pdf: $(FILE).tex
	pdflatex $(FILE)

all:
	$(FILE).pdf

clean:
	find -regex $(cleanregex) -delete

clean-p:
	find -regex $(cleanpdfregex) -delete

clean-a:
	find -regex $(cleanallregex) -delete

contents:
	./buildcontents.py
