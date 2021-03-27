# make variable that holds the foldersnames that contain a digit
FOLDERS=$(shell ls | grep -P '\d')
PDF_EX=$(addsuffix _Ex,${FOLDERS})
PDF_LEC=$(addsuffix _Lec,${FOLDERS})
PDF_SOL=$(addsuffix _Sol,${FOLDERS})
PDF=${PDF_EX} ${PDF_SOL} ${PDF_LEC}

UOSTEMPLATE=templates/beamerthemeUOS.sty templates/uoscolors.sty templates/uoslogo.sty

# create variable that removes temporary files
TEMP=.cpt .log .aux .out .bcf .nav .run.xml .toc .snm .bbl .blg
clean_temp=@rm -r _minted-* $(addprefix *,${TEMP}) 2>/dev/null || true  # never report errors

# does not create file
.PHONY: all
# rule that gets all files as prerequisites
all: $(addprefix build/,$(addsuffix .pdf,${PDF}))

# builds _Ex pdf from tex file and moves it to build
build/%_Ex.pdf: build/%_Ex.tex templates/ex_template.tex | build
	pdflatex -shell-escape $<
	mv ${@F} $@
	$(call clean_temp)

# builds _Sol pdf from tex file and moves it to build
build/%_Sol.pdf: build/%_Ex.tex templates/ex_template.tex | build
	pdflatex -shell-escape --jobname=$(basename ${@F}) '\def\solutions{}\input{$<}'
	mv ${@F} $@
	$(call clean_temp)

# builds _Lec pdf from tex file and moves it to build
build/%_Lec.pdf: build/%_Lec.tex templates/lec_template.tex ${UOSTEMPLATE} | build
	cp templates/beamerthemeUOS.sty .
	cp templates/uoscolors.sty .
	cp templates/uoslogo.sty .
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<
	-biber $(basename ${@F})
	pdflatex -shell-escape $<
	rm *.sty
	rm -f *.vrb
	mv ${@F} $@
	$(call clean_temp)

# builds _Lec tex from md file and moves it to build
build/%_Lec.tex: */%_Lec.md ${UOSTEMPLATE} | build
	cp templates/beamerthemeUOS.sty .
	cp templates/uoscolors.sty .
	cp templates/uoslogo.sty .
	pandoc -o $@ \
		-t beamer \
		--template=templates/lec_template_md.tex \
		--toc \
		--toc-depth=2 \
		--bibliography=bibliography.bib \
		--filter=pandoc-img-glob \
		--filter=bin/execute_python.py \
		--filter=bin/codeblocks.py \
		--filter=bin/fragile_slides.py \
		templates/lec_meta.yaml \
		$< 
	rm *.sty



# copy the .tex files
build/%.tex: */%.tex
	cp $< $@

# how to build from .md files
build/%_Ex.tex: */%_Ex.md
	pandoc -o $@ --template=templates/ex_template_md.tex --filter=bin/execute_python.py --filter=bin/codeblocks.py  --filter=bin/date.py --filter=pandoc-img-glob --bibliography=bibliography.bib $<


build:
	mkdir -p build

.PHONY: clean
clean:
	$(call clean_temp)
