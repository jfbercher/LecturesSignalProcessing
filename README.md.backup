# A Journey in Signal processing with Jupyter

[![Join the chat at https://gitter.im/jfbercher/LecturesSignalProcessing](https://badges.gitter.im/jfbercher/LecturesSignalProcessing.svg)](https://gitter.im/jfbercher/LecturesSignalProcessing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<a href="https://notebooks.azure.com/jfbercher/libraries/LecturesOnSignalProcessing">    <img src="https://notebooks.azure.com/launch.png" /></a>

A Series of lectures given at [ESIEE-Paris](http://www.esiee.fr), [ISBS-Paris](http://www.isbs.fr/), [ENSG](http://www.ensg.eu/)

by: J.-F. Bercher, (c) 2014-2018

We provide here the complete collection of Jupyter's notebooks, together with their html version and a <span class="info"> [PDF EBOOK](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/tex/Poly.pdf). </span>

- Notebooks are located in the subdirectory `src` and not fully executed, 
- while the html version in `html` corresponds to the full output. 

Beware that the notebooks make a heavy use of some Jupyter javascript extensions (e.g. latex_envs, exercise, ...) and unfortunately do not render correctly in nbviewer or in the github viewer ; that is the reason why we provide the static version in `./html`. See the install section below.


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

[IX - Lab on basics in image processing](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/LabImages_text.html#Lab-on-basic-image-processing)

[X - Digital filters](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/DigitalFilters.html)

[XI - Lab on Basic Filtering Problems](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/BasicFiltering_text.html)

[XII - Random Signals](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Lecture1_RandomSignals.html)

[XIII - Adaptive Filters](https://rawgit.com/jfbercher/LecturesSignalProcessing/master/html/Optimum_filtering.html#Adaptive-Filters)



## Installation
- Clone the repo as usual
- The notebooks use a bunch of nbextensions that you shall install. 

    - In particular, they need the [latex_envs extension](https://github.com/jfbercher/jupyter_latex_envs) that enable to enter and display LaTeX environments. You can install `LaTeX_envs` from pip and conda :
```
pip3 install jupyter_latex_envs [--user][--upgrade]
jupyter nbextension install --py latex_envs [--user|--sys-prefix|--system]
jupyter nbextension enable --py latex_envs [--user|--sys-prefix|--system]
```
The best option is to install these extensions from the [IPython-contrib/IPython-notebook-extensions](https://github.com/ipython-contrib/IPython-notebook-extensions) repo (also installable [from Pypi](https://pypi.org/project/jupyter_contrib_nbextensions/)). Follow the guidelines there. You may also install these extensions directly from here using:
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
### Development - Contributing - Contact

This is an ongoing work and the maturity of the different chapters varies. Actually the first chapters are much less finalized that the later ones. Feel free to make corrections, add contents, examples, information. Your contribution will be most welcome (and acknowledged). You may do so by changing the files and submitting a pull request via the github interface. 

Contact the main author, Jean-François Bercher, at jf "dot" bercher "at" gmail "dot" com
