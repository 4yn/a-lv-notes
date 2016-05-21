# LaTeX Makefile
SHELL := /bin/bash
FILE=main
cleanregex = ".+\(aux\|log\|synctex.gz\|fls\|fdb_latexmk\|bbl\|blg\)$$"

.PHONY: clean $(FILE).pdf

$(FILE).pdf: $(FILE).tex ./content
	pdflatex $(FILE)

all:
	$(FILE).pdf

clean:
	find -regex $(cleanregex) -delete

contents:
	./buildcontents.py

