PROJ := thesis

SRC	:= $(PROJ).tex
DEP	:= $(wildcard *.tex *.bib) ucithesis.cls

OUT	:= .

DVI	:= $(OUT)/$(PROJ).dvi
PDF	:= $(OUT)/$(PROJ).pdf

# Can also use pdflatex, if preferred
CMDLATEX := latex -output-directory=$(OUT)
CMDPDF   := dvipdf

PDFVIEWER := evince

all: $(DVI) $(PDF)

$(PDF) : $(DVI)
	$(CMDPDF) $(DVI) $(PDF)

# OUT directory must be ordered before we generate output
$(OUT)/%.dvi: %.tex | $(OUT)
	$(CMDLATEX) $<
	bibtex $(OUT)/$(<:%.tex=%)
	$(CMDLATEX) $<
	$(CMDLATEX) $<	# Run LaTeX again to make sure all references are correct

$(DVI) : $(DEP)

# Create the OUT directory, if it doesn't exist
$(OUT):
	mkdir -p $@

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
