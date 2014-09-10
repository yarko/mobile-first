# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -T -P
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build
GHPDIR        = mobile-first

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean build

help: build

clean:
	rm -rf $(BUILDDIR)/dirhtml/*
	rm -rf $(BUILDDIR)/doctrees/*
	(cd $(GHPDIR); git rm -rf .)

build:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) mobile-first
	@echo
	@echo "Build finished. The HTML pages are in mobile-first"

# Look at it locally before publishing it
# show: build
show:
	cd $(GHPDIR); python -m SimpleHTTPServer

checkout:
	cd $(GHPDIR)
	if [ ! -d .git ]; then\
	   	echo "no repo found to publish; see https://yarko.github.io/mobile-first/blog/gh-pages";\
		exit;\
	fi

publish: checkout
	cd $(GHPDIR)
	if [ ! -f .nojekyll ]; then\
		touch .nojekyll;\
	fi
	git add --all .
	git commit -m "Published on: $(date)"
	git push

