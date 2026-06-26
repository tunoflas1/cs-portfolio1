# Computer Science Portfolio — Uygar Tuna Oflas

A small, static computer-science portfolio built for the **B201 Computer Science Lab**
assessment at Gisma University of Applied Sciences.

🔗 **Live site:** [https://tunoflas1.github.io/cs-portfolio1/](https://tunoflas1.github.io/cs-portfolio1/)
📄 **CV (PDF):** [`cv/Uygar_Tuna_Oflas_CV.pdf`](cv/Uygar_Tuna_Oflas_CV.pdf)

> Replace `uygartunaoflas` with your actual GitHub username if it differs, in both
> the link above and in `index.html`.

## What's inside

```
cs-portfolio/
├── index.html                 # single-file portfolio site (HTML + CSS + JS)
├── cv/
│   ├── cv.tex                 # LaTeX source of the CV
│   └── Uygar_Tuna_Oflas_CV.pdf
├── projects/
│   ├── knight_path/           # shortest knight path (BFS) — Python + tests
│   │   ├── knight_path.py
│   │   └── test_knight_path.py
│   ├── text_insights/         # text statistics CLI — Python
│   │   └── text_insights.py
│   └── guestbook/             # minimal validated endpoint — PHP
│       └── guestbook.php
└── report/
    ├── report.tex             # LaTeX project report
    └── report.pdf
```

## Running the projects

```bash
# Knight path
python projects/knight_path/knight_path.py a1 h8
python -m unittest projects/knight_path/test_knight_path.py

# Text insights
python projects/text_insights/text_insights.py yourfile.txt --top 10

# Guestbook (PHP runs on a server, not on GitHub Pages)
php -S localhost:8000 -t projects/guestbook
```

## Deploying the site

1. Push this repository to GitHub.
2. **Settings → Pages → Source: `main` branch, root folder.**
3. The site goes live at `https://<username>.github.io/cs-portfolio/`.

## Tech

HTML, CSS, JavaScript (no framework), Git/GitHub, GitHub Pages, LaTeX, Python, PHP.
Fonts: Space Grotesk, Inter, JetBrains Mono (Google Fonts).
