# Basic Programming in Python


## Building files

Use the Makefile to compile Lectures, Exercise sheets and Solution sheets.

```
make  # for all files

make build/01_Introduction_Lec.pdf  # to build a specific file
```

### Requirements

- pandoc = 2.5
- pdflatex
- python >= 3.5
- and `pip install -r requirements.txt` (manual installation might be required instead)

For a walkthrough of the setup see: setup-walkthrough.txt