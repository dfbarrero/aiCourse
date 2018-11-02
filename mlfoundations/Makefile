# Customize these two lines
TARGETS=mcyte muii # Courses to compile
NAME=mlfoundations

# Do not touch
TEX=xelatex -interaction nonstopmode -halt-on-error -file-line-error
FILENAME=$(NAME).tex

.PHONY: all clean view

all : $(TARGETS)

$(TARGETS):
	$(TEX) -jobname=$(NAME)-$@ "\newcommand{\modo}{$@} \input{$(FILENAME)}"

platform=$(shell uname)
ifeq ($(platform),Darwin)
view:
	open *.pdf
else
view:
	xdg-open *.pdf
endif

clean:
	rm -f *.out *aux *bbl *blg *log *toc *.ptb *.tod *.fls *.fdb_latexmk *.lof *.nav *.snm *.vrb
