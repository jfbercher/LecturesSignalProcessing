SHELL := /bin/bash

#--> original source file in main directory
#IPYNB= $(wildcard *.ipynb)
#this is to get the list of basenames dependencies in a subdir  
IPYNB= $(notdir $(wildcard src/*.ipynb)) #$(shell ls -1 src/*.ipynb |xargs -n1 basename)

#
HTML= $(IPYNB:.ipynb=.html)
SUBDIR_HTML = $(foreach I,$(HTML),html/$I)
#alternatively:
#SUBDIR_HTML = $(addprefix html/,$(HTML))
TEX= $(IPYNB:.ipynb=.tex)
SUBDIR_TEX = $(foreach I,$(TEX),tex/$I)
SUBDIR_exec = $(foreach I,$(IPYNB),exec/$I)

here=$(CURDIR)
#/home/bercherj/JFB/tstmake


a:
	echo $(IPYNB)

rien: $(IPYNB)
	echo $(IPYNB2)
	echo $(CURDIR)  

html: $(SUBDIR_exec) $(SUBDIR_HTML)
	#jupyter nbconvert --to html $(IPYNB)
	#echo "$(SUBDIR_HTML)"

#to convert ipynb in current directory to html in sub html/
html/%.html: exec/%.ipynb
	echo "Executing jupyter nbconvert --to html $^"
	#jupyter nbconvert --to html exec/$(basename $(notdir $^)).ipynb --output html/$(basename $(notdir $^)).html
	./conversion/conv_ipynb_to_html $^	
	mv exec/$*.html html/

tex: exec $(SUBDIR_TEX)

#to convert ipynb in current directory to html in sub html/
#html/%.html: %.ipynb
#	echo "Executing jupyter nbconvert --to html $^"
#	#jupyter nbconvert --quiet --to html $^
#	./conversion/conv_ipynb_to_html $^
#	mv $*.html html/

altsrc:
	rsync -a src/ exec/ --exclude=*.ipynb

# Convert notebooks in src into an executable version in subdir exec
exec/%.ipynb: src/%.ipynb
	echo "Executing jupyter nbconvert exec $^"
	jupyter nbconvert --execute --allow-errors --to notebook $^ --output exec/$(notdir $^)

exec: altsrc $(SUBDIR_exec)

#to convert ipynb in ipynb directory to html in sub html/
html/%.html: ipynb/%.ipynb
	echo "Executing jupyter nbconvert --to html $^"
	jupyter nbconvert --quiet --to html $^
	mv $*.html html/

tex/%.tex: exec/%.ipynb
	echo "Executing jupyter nbconvert --to latex $^"
	cp $^ tex/
	cd tex/ && \
	echo "Executing jupyter $(here)/conversion/ipynb_thms_to_latex $(notdir $^)" && \
	$(here)/conversion/ipynb_thms_to_latex $(notdir $^)  #&&\
	cd ..
	rm tex/$(notdir $^)

pdf: tex
	cd tex && \
	xelatex -interaction=nonstopmode Poly.tex &> /dev/null | cat  && \
	xelatex -interaction=nonstopmode Poly.tex &> /dev/null | cat

zip: html 
	rm -f LecturesSignalProcessing.zip
	zip -9 -r LecturesSignalProcessing src/
	zip -9 -r LecturesSignalProcessing html/
	zip -9 -r LecturesSignalProcessing tex/*.pdf
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/LecturesSignalProcessing.zip  bercherj@ssh.esiee.fr:public_html/

all: tex html pdf
	cp *.css html/ 2>/dev/null | cat && \
	cp *.png html/ 2>/dev/null | cat 
	
git: all
	git add .
	git commit -m "update `date +'%y.%m.%d %H:%M:%S'`"
	git push 

sync: all
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/html/*.css  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/html/*.html  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/*.ipynb  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/tex/*.pdf  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/*.png  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/*.zip  bercherj@ssh.esiee.fr:public_html/IT3007



    rsync -av --chmod=755  -e "ssh -p 52222" $(here)/install*  bercherj@ssh.esiee.fr:public_html/IT3007

