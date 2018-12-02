from nbconvert.preprocessors import Preprocessor

class RemoveCellWithNbInit(Preprocessor):

    def preprocess(self, notebook, resources):
        notebook.cells = [cell for cell in notebook.cells if not '%run nbinit.ipy' in cell.source]
        return notebook, resources
