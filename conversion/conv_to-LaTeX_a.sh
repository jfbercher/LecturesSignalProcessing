#!/usr/bin/env bash
# example: ./conv_to-LateX.sh Lect*.ipynb


Liste=$*
#"*.ipynb"
for f in $Liste
do
  temp=${f%.ipynb}_tmp.ipynb
  cp $f  $temp
  # corrections in some markdown cells
  perl -pi -e s/'\\\\\['/'\$\$'/ $temp
  perl -pi -e s/'\\\\\]'/'\$\$'/ $temp
    # conversion ipynb vers latex
	if [[ $f == tp* ]]
	then
		echo vers "article"
    	ipython nbconvert --to latex --template jfb3_article $temp
	else
		echo vers "book"
    	ipython nbconvert --to latex --template jfb3 $temp
	fi
    ## et postprocessing
python3 thmInNb_tolatex.py ${temp%.ipynb}.tex ${f%.ipynb}.tex
python3 texheaders_rm.py ${f%.ipynb}.tex
python3 toc_and_cln.py ${f%.ipynb}.tex
  # want to number everything
  perl -pi -e s/'\\\['/'\\begin{equation}'/ ${f%.ipynb}.tex
  perl -pi -e s/'\\\]'/'\\end{equation}'/ ${f%.ipynb}.tex
done
echo Cleaning...
rm *_tmp.*
