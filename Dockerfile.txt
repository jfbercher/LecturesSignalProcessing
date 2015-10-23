FROM andrewosh/binder-base

MAINTAINER Jean-François Bercher <___@gmail.com>

USER root

# Add Julia dependencies
#RUN apt-get update
#RUN apt-get install -y julia libnettle4 && apt-get clean

USER main



# Install my custom extensions
RUN jupyter nbextension install https://rawgit.com/jfbercher/latex_envs/master/latex_envs.zip  --user
RUN jupyter nbextension enable latex_envs/latex_envs  
RUN jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/highlighter.zip  --user
RUN jupyter nbextension enable usability/highlighter/highlighter 
RUN jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/interactive_sols.zip  --user
RUN jupyter nbextension enable usability/interactive_sols/interactive_sols 

# Install requirements for Python 3
RUN /home/main/anaconda/envs/python3/bin/pip install -r requirements.txt


