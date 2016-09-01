SOURCES = Makefile bootcamp-lecture.tex slides/* code-snippets/*
TEXNAME=bootcamp-lecture
LATEX= pdflatex -shell-escape -halt-on-error

all: latex
q: $(TEXNAME).tex $(SOURCES)
	$(LATEX) $(TEXNAME)
latex: $(TEXNAME).pdf
$(TEXNAME).pdf: $(TEXNAME).tex $(SOURCES)
	$(LATEX) $(TEXNAME)
smallclean:
	rm -f $(TEXNAME).blg $(TEXNAME).bbl $(TEXNAME).aux $(TEXNAME).log $(TEXNAME).nav
clean:
	rm -f *.o \#* *~ nn $(TEXNAME).aux $(TEXNAME).log $(TEXNAME).out *.pyg *.toc $(TEXNAME).bbl $(TEXNAME).blg $(TEXNAME).nav $(TEXNAME).snm $(TEXNAME)-blx.bib $(TEXNAME).run.xml $(TEXNAME).vrb missfont.log
diff:
	git-latexdiff --main $(TEXNAME).tex -o diff.pdf -v $(OLD)
rtf:
	pdflatex -shell-escape $(TEXNAME)
	pdflatex -shell-escape $(TEXNAME)
	pdflatex -shell-escape $(TEXNAME)
	latex2rtf $(TEXNAME).tex
rerun:
	$(LATEX) $(TEXNAME)
