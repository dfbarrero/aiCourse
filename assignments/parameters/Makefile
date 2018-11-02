filename=$(shell ls *tex |cut -d'.' -f1)

.PHONY: clean

all:
	pdflatex $(filename)

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg,toc,snm,nav}
