from nbconvert.preprocessors import Preprocessor

class RemoveCellWithNbInitIpy(Preprocessor):

    def preprocess(self, notebook, resources):
        celllist = []
        for cell in notebook.cells:
            if '%run nbinit.ipy' in cell.source:
                cell.source = ''
                for output in cell.outputs:
                    if 'text' in output: 
                        output['text'] = ''            
            celllist.append(cell)
        notebook.cells = celllist
    
        return notebook, resources

 #   def preprocess_cell(self, cell, resources, index):
 #         print(type(cell))
 #         print("index ", index, " ---> ", cell.source)
 #         if cell.cell_type == "code" and "outputs" in cell:
                # Below just an ad hoc personnal filter 
 #               if "%run nbinit.ipy" in cell.source:
 #                   cell.source = 'nnnn'
                    #cell.cell_type = "code"
                    #for output in cell.outputs:
                    #    output['text'] = 'aaa'
                    #    if "data" in output: 
                    #        if 'text/html' in output.data: output.data['text/html'] = ''
                    #        if 'text/plain' in output.data: output.data['text/plain'] = ''
#                    return cell, resources
