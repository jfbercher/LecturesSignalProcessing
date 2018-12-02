# %load interactive_sols.py
from IPython.display import HTML, display, Javascript
#global cbx_id


def unhide_next_cell():
# used in case one wants to force display of next input cell (eg the cell
# with process_solution tat autohides itself)
    show = """
    var index = IPython.notebook.get_selected_index();
    var cell = IPython.notebook.get_cell(index+1);
    cell.element.find("div.input").show()
    """
    display(Javascript(show))


def unhide_all_cells():
    unhide_all = """
          var start = 0 //IPython.notebook.get_selected_index();
          var end = IPython.notebook.ncells()
          for (var i=start; i<end; i++) { 
              console.log(i)
              IPython.notebook.select(i);
              var cell = IPython.notebook.get_selected_cell();
              cell.element.show();  
              cell.element.find("div.input").show();
              cell.element.find("div.output").show()
                    }                                
        """
    display(Javascript(unhide_all))


def get_cbx_id():
    # This is to get the current checkbox id. The ids are incremented each time a checkbox is created.
    # The current max id is store in the notebook's metadata

    get_cbx_id = """
    var kernel = Jupyter.notebook.kernel;
    if (kernel!=undefined){
        //var command = "cbx_id = '" +  Jupyter.notebook.metadata.interactive_sols.cbx_id + "'";
        var command = "cbx_id = " +  Jupyter.notebook.metadata.interactive_sols.cbx_id ;
        kernel.execute(command);
        console.log('cfg.cbx_id',Jupyter.notebook.metadata.interactive_sols.cbx_id);}
    """

    # Ater execution (and display), we will get the saved value for cbx_id
    display(Javascript(get_cbx_id))  # get the current id in variable cbx_id


def process_solution(nb_cells_to_process=1):

    #global cbx_id
    #cbx_id = int(cbx_id)
    
    # mychbox is a standard checkbox
    myhchbox = """
    Show solution: <input type="checkbox"  id="myCheck{0}" 
       onclick="console.log(document.getElementById('myCheck{0}').checked ? show_input({1}) : hide_input({1}))" 
       //onclick="console.log(document.getElementById('myCheck{0}').checked ?  click_on("myCheck{0}",{1}) : click_off("myCheck{0}",{1}))" 
       checked>
       <script> 
       //init_cell_sols("myCheck{0}"); 
       cfg= Jupyter.notebook.metadata.interactive_sols;
       var cell = IPython.notebook.get_selected_cell();
         //cell.metadata.manualexec = true; 
         cell.metadata.widget = true;
         cell.metadata.cbox_id = "myCheck{0}";
         cell.metadata.cbox_ck = true;
         cfg.cbx_id+=1;
         cell.element.find("div.input").hide(); //hide itself...
       </script>
    """

    # myhchboxb is a pretty checkbox with css
    myhchboxb = """
    <div class="onoffswitch">
        <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" 
        onclick="console.log(document.getElementById('myCheck{0}').checked ? show_input({1}) : hide_input({1}))" 
        id="myCheck{0}"  checked>
        <label class="onoffswitch-label" for='myCheck{0}'>
            <span class="onoffswitch-inner"></span>
            <span class="onoffswitch-switch"></span>
        </label>
    </div>
    <script>
        if (init_cell_sols!==undefined) {{
        init_cell_sols({0})
        IPython.notebook.kernel.execute('cbx_id = int(cbx_id)+1 ')
        }} else console.log("on reload init cell undefined")
    </script>
    """

    #var cell = IPython.notebook.get_cell(index+1);
    #cell.element.find("div.input").show()

# myhchboxd is a pretty checkbox with css
    myhchboxd = """
    <script>
        console.log(typeof pr_cell_sols)
        if (typeof pr_cell_sols !== "undefined") {{
        pr_cell_sols({0})
        }} else console.log("on reload, process_cell undefined")
    </script>
    """


    #display(HTML(myhchboxb.format(cbx_id,nb_cells_to_process))) # display
    display(HTML(myhchboxd.format(nb_cells_to_process))) # display
    # the checkbox