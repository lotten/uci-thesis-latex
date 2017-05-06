PROJ := thesis

SRC	:= $(PROJ).tex
DEP	:= $(wildcard *.tex *.bib) ucithesis.cls

OUT	:= .

PDF	:= $(OUT)/$(PROJ).pdf

# Can also use pdflatex, if preferred
CMDLATEX := pdflatex -output-directory=$(OUT)

PDFVIEWER := evince

all: $(PDF)


# OUT directory must be ordered before we generate output
$(OUT)/%.pdf: %.tex | $(OUT)
	$(CMDLATEX) $<
	bibtex $(OUT)/$(<:%.tex=%)
	$(CMDLATEX) $<
	$(CMDLATEX) $<	# Run LaTeX again to make sure all references are correct

$(PDF) : $(DEP)

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
