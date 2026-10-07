# antonreinicke.com

Personal academic website — plain HTML and CSS. No build step, no JavaScript,
and no third-party requests: fonts, icons and the CV are all served from here.

    index.html        all content
    style.css         all styling; the knobs are the CSS variables at the top
    assets/cv.pdf     built from ../cv/academic/Anton_Reinicke_CV.tex
    assets/fonts/     Roboto, self-hosted (Apache-2.0)
    assets/icons/     brand icons (Simple Icons)
    serve.py          local preview on http://localhost:8787, no caching

GitHub Pages serves this repo from `main` at the root. `CNAME` holds the custom
domain; `.nojekyll` tells Pages to serve the files as-is rather than running
them through Jekyll.

An earlier layout is kept in ../archive/v1/, outside this repo.
