SHELL := /bin/bash

#--> original source file in main directory
#IPYNB= $(wildcard *.ipynb)
#this is to get the list of basenames dependencies in a subdir  
IPYNB= $(notdir $(wildcard src/*.ipynb)) #$(shell ls -1 src/*.ipynb |xargs -n1 basename)

#
MAIN_TeX="Poly.tex"
MAIN_pdf="Poly.pdf"
zip_dest="public_html/PPMD/"
web_dest="public_html/Lectures_SignalProcessing"
ssh_user="bercherj@ssh.esiee.fr"
#
HTML= $(IPYNB:.ipynb=.html)
SUBDIR_HTML = $(foreach I,$(HTML),html/$I)
#alternatively:
#SUBDIR_HTML = $(addprefix html/,$(HTML))
TEX= $(IPYNB:.ipynb=.tex)
SUBDIR_TEX = $(foreach I,$(TEX),tex/$I)
SUBDIR_exec = $(foreach I,$(IPYNB),exec/$I)

here=$(CURDIR)
dirName=$(notdir $(CURDIR))

html: $(SUBDIR_HTML) $(SUBDIR_exec)

#to convert ipynb in current directory to html in sub html/
html/%.html: exec/%.ipynb
	echo "Executing jupyter nbconvert --to html_with_toclenvs $^"
	jupyter nbconvert --to html_with_toclenvs $^
	./update_html $^
	#perl -pi -e s/_fr}/-fr}/g $^
	mv exec/$*.html html/
	rsync -a src/ html/ --exclude='*.ipynb' --exclude='*.html' --exclude='*.*py'

tex: exec $(SUBDIR_TEX)

altsrc:
	rsync -a src/ exec/ --exclude='*.ipynb'

# Convert notebooks in src into an executable version in subdir exec
exec/%.ipynb: src/%.ipynb
	echo "Executing jupyter nbconvert exec $^"
	jupyter nbconvert --execute --allow-errors --to notebook $^ --output-dir exec 

exec: altsrc $(SUBDIR_exec)


tex/%.tex: exec/%.ipynb
	echo "Executing jupyter nbconvert --to latex_with_lenvs $^"
	cp $^ tex/
	cd tex/ && \
    jupyter nbconvert --to latex_with_lenvs --LenvsLatexExporter.removeHeaders=True --template thmsInNb_book $(notdir $^)  &&\
	cd .. &&\
	rm tex/$(notdir $^)

tex/$(MAIN_pdf): $(SUBDIR_TEX)
	echo Compiling $(MAIN_TeX) to pdf in tex directory
	rsync -a src/*.png tex/ && \
	cd tex && \
	xelatex -interaction=nonstopmode $(MAIN_TeX) &> /dev/null | cat  && \
	xelatex -interaction=nonstopmode $(MAIN_TeX) &> /dev/null | cat

pdf: tex/$(MAIN_pdf) $(SUBDIR_TEX)

zip: html 
	rm -f $(dirName).zip
	zip -9 -r $(dirName) src/
	zip -9 -r $(dirName) html/
	zip -9 -r $(dirName) tex/*.pdf
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/$(dirName).zip  $(ssh_user):$(zip_dest)

all: tex html pdf
	cp *.css html/ 2>/dev/null | cat && \
	cp *.png html/ 2>/dev/null | cat 
	
git: all
	git add .
	git commit -m "update `date +'%y.%m.%d %H:%M:%S'`"
	git push 

sync: 
	perl -pi -e s/.ipynb/.html/g $(here)/html/*.html
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/html/*.* --exclude='*.ipynb' $(ssh_user):$(web_dest)
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/exec/*.ipynb  $(ssh_user):$(web_dest)
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/exec/*.ipy  $(ssh_user):$(web_dest)
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/exec/*.py  $(ssh_user):$(web_dest)
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/tex/*.pdf  $(ssh_user):$(web_dest)

$(V).SILENT:



