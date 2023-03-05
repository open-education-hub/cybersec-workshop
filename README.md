# Cybersercurity Workshop

A collection of demos and challenges fit to be used during a 2-hour workshop followed by a CTF.

## Slides

To build [slides](./slides), install [`reveal-md`](https://github.com/webpro/reveal-md).
Slides are built into a web site.
Then, while inside the `slides/` directory, run `make` and open the `_site/index.html` file in a browser:

```console
.../slides$ ls
Makefile  slides.md

.../slides$ make
reveal-md slides.md --static _site
❏ reveal-md/node_modules/reveal.js/dist → _site/dist
❏ reveal-md/node_modules/reveal.js/plugin → _site/plugin
❏ reveal-md/node_modules/highlight.js/styles/base16/zenburn.css → _site/css/highlight/base16/zenburn.css
★ _site/slides.html
❏ _site/slides.html → _site/index.html
❏ /usr/local/lib/node_modules/reveal-md/lib/favicon.ico → _site/favicon.ico
Wrote static site to _site

.../slides$ open _site/index.html
```

## Works Items

Start with the [Demos](./demos/).

Then solve the [Challenges](./challenges/).

Submit flags on the [CTF Platform](https://workshop-ctf.security.cs.pub.ro/).
You need to register an account.
Then see the [scoreboard](https://workshop-ctf.security.cs.pub.ro/scores) as you submit flags.
