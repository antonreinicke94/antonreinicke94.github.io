# antonreinicke.com

Personal academic website — plain HTML and CSS, no build step and no
external dependencies (fonts and icons are served from this repo, so
no third-party requests are made when the page loads).

    index.html        all content
    style.css         all styling; the knobs are the CSS variables at the top
    assets/cv.pdf     CV, built from ../cv/academic/Anton_Reinicke_CV.tex
    assets/icons/     brand icons (Simple Icons set)
    serve.py          local preview on http://localhost:8787, no caching

GitHub Pages serves this repo from `main` at the root. `CNAME` holds the
custom domain and `.nojekyll` tells Pages to serve the files as-is.
