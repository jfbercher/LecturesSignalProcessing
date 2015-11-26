# A Journey in Signal processing with IPython

A Series of lectures given at [ESIEE-Paris](http://www.esiee.fr), [ISBS-Paris](http://www.isbs.fr/), [ENSG](http://www.ensg.eu/)

by: J.-F. Bercher

We provide here the complete collection of Jupyter's notebooks, together with their html version and a [pdf ebook](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/tex/Poly.pdf).
Notebooks are located in the subdirectory `src` and not fully executed, while the html version in `html` corresponds to the full output. Beware that the notebooks make a heavy use of some Jupyter javascript extensions (e.g. latex_envs, exercise, ...) and unfortunately do not render correctly in nbviewer or in the github viewer ; that is the reason why we provide the static version in `./html`. See the install section below.


## Table of Contents
 
The full table of contents is [here](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/index.html). 
Below are the chapter heads. 

 [I - Effects of delays and scaling on signals](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/DelaysAndScales.html)

 [II - A basic introduction to filtering](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Intro_Filtering.html)

[III -Introduction to the Fourier representation](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Intro_Fourier.html)

[IV - Fourier transform](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Fourier_transform.html)

[V - Convolution](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Convolution.html)

[VI - Lab on Basic System Representations](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Exercises_BasicSystemsRepr.html)

[VII - The continuous time case](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Continuous_time_case.html)

[VIII - Periodization, discretization and sampling](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Periodization_discretization.html)

[IX - Lab on basics in image processing (text)](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/LabImages_text.html#Lab-on-basic-image-processing)

[X - Digital filters](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/DigitalFilters.html)

[XI - Lab on Basic Filtering Problems](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/BasicFiltering_text.html)

[XII - Random Signals](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Lecture1_RandomSignals.html)

[XIII - Adaptive Filters](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Optimum_filtering.html#Adaptive-Filters)



## Installation
- Clone the repo as usual
- The notebooks use a bunch of nbextensions that you shall install. In particular, they need the latex_envs extension that enable to enter and display LaTeX environments. The best option is to install these extensions from the [IPython-contrib/IPython-notebook-extensions](https://github.com/ipython-contrib/IPython-notebook-extensions) repo. Follow the guidelines there. You may also install these extensions directly from here using:
```bash
	# Install jupyter extensions
	jupyter nbextension install https://rawgit.com/jfbercher/latex_envs/master/latex_envs.zip  --user
	jupyter nbextension enable latex_envs/latex_envs  
	jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/highlighter.zip  --user
	jupyter nbextension enable usability/highlighter/highlighter 
	jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/interactive_sols.zip  --user
	jupyter nbextension enable usability/interactive_sols/interactive_sols 
	jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/exercise.zip  --user
	jupyter nbextension enable usability/exercise/main 
	jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/exercise2.zip  --user
	jupyter nbextension enable usability/exercise2/main 
	jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/rubberband.zip  --user
	jupyter nbextension enable usability/rubberband/main 
```


----
<div style="display:block; color: #CC0099;"> Comments, issues, contributions (PR) are most welcome. If you are happy with these documents, you may drop me a note or make an issue to say it. </div>
