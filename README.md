uci-thesis-latex
================

### A LaTeX template for thesis and dissertation documents at UC Irvine.

Adapted from a blog post here:

- http://vocaro.com/trevor/blog/2008/01/08/a-latex-template-for-uci-dissertations/

Credit goes to Trevor, author of the site above, and those students
who he inherited the template from (see the change log in the cls
file).

However, it seems the site above isn't actively maintained anymore, so
I reorganized and updated things a bit to comply (to the best of my
knowledge) with the latest UCI Theses and Dissertation Manual for
electronic filing as of Fall 2013:

- http://special.lib.uci.edu/dissertations/electronic/tdmanuale.html

#### Download

The template homepage is:
- https://github.com/lotten/uci-thesis-latex

A zip archive of the latest version is available directly at:
- https://github.com/lotten/uci-thesis-latex/archive/master.zip

#### Usage

The main file is `thesis.tex`, from which a number of other files are
included. Take a look at the comments in the LaTeX sources for some
more specific pointers.

To compile, simply run `thesis.tex` through your LaTeX executable of
choice. I've tested with `latex`+`dvipdf` on Linux, but `pdflatex` and
others should work equally well. An optional, simple makefile to
automate some of the steps is also included (adapted from Trevor,
customize to suit your needs).

#### Disclaimer

Even though UCI Special Collections and Archives has referred students
to this template, it is _not officially maintained by UCI_ and provided
here _without any guarantees whatsoever_.

That being said, I believe it can be genuinely useful to future grad
students and I'll try my best to maintain it going forward. So if you
find anything that is at odds with UCI requirements, now or in the
future, or have other suggestions feel free to submit a pull request
on GitHub or contact me directly (lotten _at_ uci _dot_ edu).
