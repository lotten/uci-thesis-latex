PROJ = thesis

SRC	= $(PROJ).tex
DEP	= *.tex

OUT	= .

DVI	= $(OUT)/$(PROJ).dvi
PDF	= $(OUT)/$(PROJ).pdf

CMDLATEX = latex -output-directory=$(OUT)
CMDPDF   = dvipdf

PDFVIEWER = evince

$(DVI) : $(DEP)
	make tex

$(PDF) : $(DVI)
	$(CMDPDF) $(DVI) $(PDF)

tex	:
	mkdir -p $(OUT)
	$(CMDLATEX) $(SRC)

all :
	make tex
	make bib
	make tex
	make tex    # Run LaTeX again to make sure all references are correct

bib	:
	bibtex $(OUT)/$(PROJ)

show	: $(PDF)
	$(PDFVIEWER) "$(PDF)"

clean	:
	rm -rf $(OUT)/*.aux
	rm -rf $(OUT)/*.bbl
	rm -rf $(OUT)/*.blg
	rm -rf $(OUT)/*.dvi
	rm -rf $(OUT)/*.lof
	rm -rf $(OUT)/*.log
	rm -rf $(OUT)/*.lot
	rm -rf $(OUT)/*.out
	rm -rf $(OUT)/*.toc
	rm -rf $(OUT)/*.pdf
