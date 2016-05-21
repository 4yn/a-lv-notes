# LaTeX Makefile
SHELL := /bin/bash
FILE=main
cleanregex = ".+\(aux\|log\|synctex.gz\|fls\|fdb_latexmk\)$$"

$(FILE).pdf: $(FILE).tex
	pdflatex $(FILE)

all:
	$(FILE).pdf

.PHONY: clean
clean:
	find -regex $(cleanregex) -delete

