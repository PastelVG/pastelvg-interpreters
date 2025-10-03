# PastelVG Interpreters (for v 1.0 SVG only ) 

> Python-based tools for working with the [PastelVG](https://www.pastelvg.com) vector graphics format.

---

## ✨ What is this?

This repository contains the official Python interpreter and CLI for the [PastelVG](https://github.com/pastelvg/specification) format — a friendly, JSON-based alternative to SVG.

It includes tools to:

- 🔄 Convert SVG → PastelVG JSON
- 🔁 Convert PastelVG → SVG (round-trip safe)
- 🛠 Parse and manipulate `.pvg.json` files programmatically
- 🧪 Validate elements against the spec

---

## 🚀 Quick Start

# Clone the repo
git clone https://github.com/PastelVG/pastelvg-interpreters.git
cd pastelvg-interpreters

# Run the CLI
python pastelvg_cli.py test.svg --to-pastelvg

# Or output to a file
python pastelvg_cli.py test.svg --to-pastelvg -o out.pvg.json



### Project Structure
pastelvg/
├── parser.py       # Parses SVG into PastelVG
├── converter.py    # Handles conversion logic
cli/
└── pastelvg.py     # Command-line interface

### Dependencies
Python 3.8+
No third-party packages (pure stdlib, zero install needed)

### 🧪 Test Files
Check the examples/ folder for ready-to-try files.

###📄 License
Licensed under the Apache 2.0 License.
Copyright © 2025 Aeon Development Group

🌈 About PastelVG
PastelVG is a lightweight, declarative vector graphics format built for:
Educational tools
Creative software
Visual editors
Procedural and generative art
It’s easy to read, JSON-native, and designed to bring joy to 2D graphics workflows.
See pastelvg.com for full spec and docs | website being built
