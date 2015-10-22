IPYNB= $(wildcard *.ipynb)
#this is to get the list of basenames dependencies in a subdir  
IPYNBsub= $(shell ls -1 ipynb/*.ipynb |xargs -n1 basename)

HTML= $(IPYNB:.ipynb=.html)
SUBDIR_HTML = $(foreach I,$(HTML),html/$I)
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

tex: $(SUBDIR_TEX)

#to convert ipynb in current directory to html in sub html/
#html/%.html: %.ipynb
#	echo "Executing jupyter nbconvert --to html $^"
#	#jupyter nbconvert --quiet --to html $^
#	./conversion/conv_ipynb_to_html $^
#	mv $*.html html/

# Convert notebooks in an executable version
exec/%.ipynb: %.ipynb
	echo "Executing jupyter nbconvert exec $^"
	jupyter nbconvert --execute --allow-errors --to notebook $^ --output exec/$^

exec: $(SUBDIR_exec)

#to convert ipynb in ipynb directory to html in sub html/
html/%.html: ipynb/%.ipynb
	echo "Executing jupyter nbconvert --to html $^"
	jupyter nbconvert --quiet --to html $^
	mv $*.html html/

tex/%.tex: %.ipynb
	echo "Executing jupyter nbconvert --to latex $^"
	cp $^ tex/
	cd tex/ && \
	#jupyter nbconvert --quiet --to latex $^ && \
	#mv $*.tex tex/ && \
    	$(here)/conversion/ipynb_thms_to_latex $^ &&\
	cd ..
	rm tex/$^

pdf: tex
	cd tex && \
	xelatex -interaction=nonstopmode Poly.tex &> /dev/null && \
	xelatex -interaction=nonstopmode Poly.tex &> /dev/null 

all: tex html pdf
	cp *.css html/
	cp *.png html/
	
sync: all
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/html/*.css  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/html/*.html  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/*.ipynb  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/tex/*.pdf  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/*.png  bercherj@ssh.esiee.fr:public_html/IT3007
	rsync -av --chmod=755  -e "ssh -p 52222" $(here)/*.zip  bercherj@ssh.esiee.fr:public_html/IT3007
    rsync -av --chmod=755  -e "ssh -p 52222" $(here)/install*  bercherj@ssh.esiee.fr:public_html/IT3007



o
oa
