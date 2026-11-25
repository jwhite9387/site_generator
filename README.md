# Static Site Generator

A Markdown-to-HTML static site generator written in Python with no external dependencies. It converts a folder of Markdown files into a complete website.

**Live demo:** https://jwhite9387.github.io/site_generator/

Built as part of the [Boot.dev](https://www.boot.dev) backend curriculum, then extended with HTML escaping, a parser-order bug fix, and additional tests.

## Features

- **Block-level parsing:** headings, paragraphs, block quotes, ordered and unordered lists, and fenced code blocks
- **Inline parsing:** bold, italic, inline code, links, and images
- **Recursive HTML node tree** that renders the whole page in a single traversal
- **Template system** with title and content placeholders
- **Configurable base path** so the site works under a GitHub Pages subdirectory
- **HTML escaping** so raw HTML in Markdown displays as text instead of executing
- **49 unit tests** (Python `unittest`) covering each stage of the parser

## How it works

1. The Markdown file is split into blocks, and each block is classified by type.
2. Inline text inside each block is tokenized into typed nodes (text, bold, italic, code, link, image).
3. Nodes are converted into an HTML node tree (leaf and parent nodes).
4. The tree renders to an HTML string, which is inserted into `template.html`.
5. Pages are written to `docs/`, mirroring the structure of `content/`.

## Usage

Requires Python 3.12+ No packages to install.

```bash
./build.sh   # build for deployment (base path /site_generator/)
./main.sh    # build and preview locally at http://localhost:8888
./test.sh    # run the test suite
```

Put Markdown files in `content/` and static assets (CSS, images) in `static/`. Output goes to `docs/`.

## Project structure

```
content/     Markdown source pages
static/      CSS and images copied to the output
template.html  Page template
src/         Parser, node classes, and build script
docs/        Generated site (served by GitHub Pages)
```

## Known limitations

- Nested lists and nested inline formatting (e.g., italic inside bold) are not supported
- Code blocks can't contain blank lines
- Link URLs containing parentheses are not handled
- Italics use `_underscores` only

## Possible next steps

- Support blank lines inside fenced code blocks
- Refactor the duplicated image and link splitting functions
- Add incremental builds
