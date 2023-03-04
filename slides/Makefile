RVMD = reveal-md

SLIDES = slides.md
SITE = _site
OPEN = xdg-open

.PHONY: all html clean

all: html

html: $(SITE)

$(SITE): $(SLIDES)
	$(RVMD) $(SLIDES) --static $@

open: $(SITE)
	$(OPEN) $</index.html

clean:
	-rm -f *~
	-rm -fr $(SITE)
