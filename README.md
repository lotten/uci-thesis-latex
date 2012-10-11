uci-thesis-latex
================

### A LaTeX template for thesis and dissertation documents at UC Irvine.

Adapted from a blog post here:

- http://vocaro.com/trevor/blog/2008/01/08/a-latex-template-for-uci-dissertations/

Credit goes to Trevor, author of the site above, and those students
who he inherited the template from (see the change log in the cls
file)!

However, it seems the site above isn't actively maintained anymore, so
I reorganized and updated things a bit to comply (to the best of my
knowledge) with the latest UCI Theses and Dissertation Manual for
electronic filing as of Fall 2012:

- http://special.lib.uci.edu/dissertations/electronic/tdmanuale.html

Naturally, this template comes _without any guarantees whatsoever_,
but if you find anything that's at odds with UCI requirements, now or
in the future, feel free to submit a pull request or contact me
directly.

#### Usage

Simply run `thesis.tex` through your LaTeX executable of choice. The
template has been tested with `latex`+`dvipdf`, but `pdflatex` and
others should work equally well. An optional, simple makefile to
automate some of the steps is also included (adapted from Trevor).
