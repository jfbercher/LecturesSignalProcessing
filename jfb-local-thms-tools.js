// Allow Python-code in markdown cells
// Encapsulate using {{...}}
// - You can also return html or markdown from your Python code
// - You can embed images, however they will be sanitized on reload.

var eqNum=0; // begins equation numbering at eqNum+1
var eqLabelWithNumbers=true; //if true, label equations with equation numbers; otherwise using the tag specified by \label
var conversion_to_html=false;

var run_this = function () {
    var load_ipython_extension = function () {
    "use strict";
    if (IPython.version[0] != 2) {
        console.log("This extension requires IPython 2.x")
        return
    }
    
    var security = IPython.security;
    var _on_reload = true; /* make sure cells with variables render on reload */

/*********/
	var thmInNb = function (text) {

		// IPython static_path dir relative to here:
		//var static_path = "/usr/local/lib/python3.3/dist-packages/IPython/html/static/";

		//var fs = require('fs');
		//var IPython;
		// 
		//var marked = require(static_path + 'components/marked/lib/marked.js');
		//eval(fs.readFileSync(static_path + "base/js/namespace.js", 'utf8'));
		//eval(fs.readFileSync(static_path + "base/js/utils.js", 'utf8'));
		//eval(fs.readFileSync(static_path + "notebook/js/mathjaxutils.js", 'utf8'));
   
            var eqLabNums = {};
			var thmCounter  = { num: 0 };
			var excsCounter = { num: 0 };
			var environmentMap = {
			    thm: 	  { title: "Theorem"    ,counter: thmCounter  },
			    lem:  	  { title: "Lemma"      ,counter: thmCounter  },
			    cor:   	  { title: "Corollary"  ,counter: thmCounter  },
			    prop:  	  { title: "Property"   ,counter: thmCounter  },
			    defn:  	  { title: "Definition" ,counter: thmCounter  },
			    rem:   	  { title: "Remark"     ,counter: thmCounter  },
			    prob:  	  { title: "Problem"    ,counter: excsCounter },
			    excs:  	  { title: "Exercise"   ,counter: excsCounter },
			    examp: 	  { title: "Example"    ,counter: excsCounter },
                property:  	  { title: "Property"   ,counter: thmCounter  },
			    theorem:   	  { title: "Theorem"    ,counter: thmCounter  },
			    lemma:   	  { title: "Lemma"      ,counter: thmCounter  },
			    corollary:    { title: "Corollary"  ,counter: thmCounter  },
			    proposition:  { title: "Property"   ,counter: thmCounter  },
			    definition:   { title: "Definition" ,counter: thmCounter  },
			    remark:   	  { title: "Remark"     ,counter: thmCounter  },
			    problem:  	  { title: "Problem"    ,counter: excsCounter },
			    exercise:     { title: "Exercise"   ,counter: excsCounter },
			    example: 	  { title: "Example"    ,counter: excsCounter },
			    itemize: 	  { title: "Itemize"     },
			    enumerate: 	  { title: "Enumerate"    },
                textboxa: 	  { title: " "  },
			    proof: 	  { title: "Proof" }
			};

		{ //****************************************************************************
		var EnvReplace = function (message) {
//console.log(message);

//Look for pairs [ ]
		    	var message = message.replace(/^(?:<p>)?\[([\s\S]*?)^(?:<p>)?\]/gm,
function (wholeMatch, m1) {
//return "\\["+m1+"\\]";
m1=m1.replace(/<[/]?em>/g,"_"); //correct possible incorrect md remplacements in eqs
m1=m1.replace(/left{/g,"left\\{"); //correct possible incorrect md remplacements in eqs
return "\\["+m1+"\\]";
}
 );

		    	var message = message.replace(/(?:<p>)?([$]{1,2})([\s\S]*?)(?:<p>)?\1/gm,
function (wholeMatch, m1) {
//return "\\["+m1+"\\]";
wholeMatch=wholeMatch.replace(/<[/]?em>/g,"_"); //correct possible incorrect md remplacements in eqs
wholeMatch=wholeMatch.replace(/left{/g,"left\\{"); //correct possible incorrect md remplacements in eqs
return wholeMatch;
}
 );

//			var message = message.replace(/^\]/gm, "\\]");

//console.log(message);
			//while (message.match(/\\begin{(\w+)}([\s\S]*?)\\end{\1}/gm)!="") {
			var out = message.replace(/\\begin{(\w+)}([\s\S]*?)\\end{\1}/gm, function (wholeMatch, m1, m2) {


				//if(!environmentMap[m1]) return wholeMatch;
				var environment = environmentMap[m1];
				if(!environment) return wholeMatch;
				var title = environment.title;
				if(environment.counter) {
				    environment.counter.num++;
				    title += ' ' + environment.counter.num;
				}
				//The conversion machinery (see marked.js or mathjaxutils.js) extracts text and math and converts text to markdown. 
				//Here, we also want to convert thm like env. 
				//So we do it here. However, environments with blank lines are *not* extracted before and thus already converted. 
				// Thus we avoid to process them again.
				// Try to check if there is remaining Markdown
				// |\n\s-[\s]*(\w+)/gm
				// /\*{1,2}([\s\S]*?)\*{1,2}|\_{1,2}([\s\S]*?)\_{1,2}/gm)
				if (m2.match(/\*{1,2}([\s\S]*?)\*{1,2}|\_{1,2}([\S]*?)\_{1,2}|```/gm)) { 
				   var m2 = marked.parser(marked.lexer(m2));}
		
	
				var result = '<div class="latex_' + m1 + '"><span class="latex_title">'+ title + '</span>' + m2;

				if (m1 == "proof") {
				    result += '<span class="latex_proofend" style="float:right">■</span>';
				}

				if (m1=="itemize"){
				var result="<div><ul>"+m2.replace(/\\item/g,"<li>")+"</ul>";
						};

				if (m1=="enumerate"){
				var result="<div><ol>"+m2.replace(/\\item/g,"<li>")+"</ol>";
							};

				result=EnvReplace(result); //try to do further replacements
				return result + '</div>';
			    });
			//out = EnvReplace(out);

		return out; //}

		}
		} //**********************************************************************************


			{
			// This is to replace references by links to the correct environment, 
			//while preserving links to equations
			// which are worked out by MathJax

                 //LABELS
			     var text = text.replace(/\\label{(\S+):(\S+)}/g, function (wholeMatch, m1, m2) {
                 m2=m2.replace(/<[/]?em>/g,"_");
                 if (m1 =="eq") {
                    if (conversion_to_html) {
				      /*  if (eqLabelWithNumbers) {
					    eqNum++;
					    return wholeMatch + '\\tag{'+eqNum+'}' ;
				       */                         
				       return wholeMatch; //+ '\\tag{'+m1+':'+m2+'}' ; 
                                            }
                    else{                       
				    if (eqLabelWithNumbers) {
					eqNum++;
					//return '<a id="' + m1 + m2 + '">' + '['+m1+':'+m2+']' + '</a>' + '\\tag{'+eqNum+'}' ;
                    eqLabNums[m2]= eqNum.toString();

                    return  '\\tag{'+eqNum+'}' ;
				                            }
				   //return '<a id="' + m1 + m2 + '">' + '['+m1+':'+m2+']' + '</a>' + '\\tag{'+m1+':'+m2+'}' ;
                   // return  '\\tag{'+m1+':'+m2+'}' ;  
                   return  '\\tag{'+m2+'}' ;  
					                        };
                               }
			   return '<a id="' + m1 + m2 + '">' + '['+m1+':'+m2+']' + '</a>'; }
						);


           //REFERENCES
		   var text = text.replace(/\\ref{(\S+):(\S+)}/g, function (wholeMatch, m1, m2) {
                 m2=m2.replace(/<[/]?em>/g,"_");
                if (conversion_to_html) {
				    if (m1 =="eq") return wholeMatch;}
                else{
                    if (m1 =="eq") {
                        if (eqLabelWithNumbers) {
                                return eqLabNums[m2]; } 
                        else return m1+':'+m2;}  
                    }

				return '<a class="latex_ref" href="#' + m1  + m2 + '">' +'['+m1+':'+m2+']'+ '</a>';
			    });      


	
			   {	
			//This is to substitute simple LaTeX+argument commands 
			var cmdsMap = {
				    underline: 	  { replacement: "u"  },
				    textit: 	  { replacement: "i"  },
				    textbf: 	  { replacement: "b"  },
				    textem: 	  { replacement: "em"  },
				    section: 	  { replacement: "h1"  },
				    subsection:   { replacement: "h2"  },
				      }

			text=EnvReplace(text);		

////--------------------
//// This is to replace references by links to the correct environment, 
//			//while preserving links to equations
//			// which are worked out by MathJax
//			   var text = text.replace(/\\ref{(\w+):(\w+)}/g, function (wholeMatch, m1, m2) {
//				//if (m1 =="eq") return wholeMatch; 
//				return '<a class="latex_ref" href="#' + m1  + m2 + '">' +'['+m1+':'+m2+']'+ '</a>';
//			    });      
//			   var text = text.replace(/\\labele{(\w+):(\w+)}/g, function (wholeMatch, m1, m2) {
//			      /* if (m1 =="eq") {
//				    if (eqLabelWithNumbers) {
//					eqNum++;
//					return wholeMatch + '\\tag{'+eqNum+'}' ;
//				     }
//				   return wholeMatch + '\\tag{'+m1+':'+m2+'}' ; */
//                                if (m1 =="eq") {
//				    if (eqLabelWithNumbers) {
//					eqNum++;
//					return '<a id="' + m1 + m2 + '">' + '['+m1+':'+m2+']' + '</a>' + '\\tag{'+eqNum+'}' ;
//				     }
//				   return '<a id="' + m1 + m2 + '">' + '['+m1+':'+m2+']' + '</a>' + '\\tag{'+m1+':'+m2+'}' ; 
//				
//					     }
//			   return '<a id="' + m1 + m2 + '">' + '['+m1+':'+m2+']' + '</a>'; }
//						);
////--------------------	 

			 var text = text.replace(/\\([\w]*){(.+?)}/g, function (wholeMatch, m1,m2) {
		
				      var cmd = cmdsMap[m1];
				      if (!cmd) return wholeMatch;
				      var tag=cmd.replacement;
				      return '<'+tag+'>' + m2  +  '</'+tag+'>';
				    });

                         //Other small replacements
 				    var text = text.replace(/\\index{(.+?)}/g, function (wholeMatch, m1) {   
				      return '';
				    });
				     var text = text.replace(/\\noindent/g, "");
				     var text = text.replace(/\\(?:<\/p>)/g, "</p>");
 				   


			}

	     	

			   return text;
			};
	


		};





    var load_css = function (name) {
        var link = document.createElement("link");
        link.type = "text/css";
        link.rel = "stylesheet";
        link.href = require.toUrl(name);
        link.href = name;
       // console.log(name);
       // console.log(link);
        document.getElementsByTagName("head")[0].appendChild(link);
        
      };


/*********/
    


    /* Override original markdown render function */
    
    IPython.MarkdownCell.prototype.render = function () {
        var cont = IPython.TextCell.prototype.render.apply(this);
        
        cont = cont || IPython.notebook.dirty || _on_reload
        if (cont) {
            var text = this.get_text();
            var math = null;
            if (text === "") { text = this.placeholder; }
            var text_and_math = IPython.mathjaxutils.remove_math(text);
            text = text_and_math[0];
            math = text_and_math[1];
            var html = marked.parser(marked.lexer(text));
            html = IPython.mathjaxutils.replace_math(html, math);
            html = thmInNb(html);  //<----- thmInNb patch here
            html = security.sanitize_html(html);
            html = $($.parseHTML(html));
            // links in markdown cells should open in new tabs
            html.find("a[href]").not('[href^="#"]').attr("target", "_blank");
            this.set_rendered(html);
            this.element.find('div.input_area').hide();
            this.element.find("div.text_cell_render").show();
            this.typeset();

        }
        return cont
    };
    

    /* show values stored in metadata on reload */
    $([IPython.events]).on('status_started.Kernel', function () { 
        
        var ncells = IPython.notebook.ncells()
        var cells = IPython.notebook.get_cells()
        for (var i=0; i<ncells; i++) { 
            var cell=cells[i];
            cell.render();
             }
        _on_reload = false;
    })

    load_css('./jfb-local-thms-tools.css');
    console.log("Loading ./jfb-local-thms-tools.css");

var init_cells = function () { 
        
        var ncells = IPython.notebook.ncells()
        var cells = IPython.notebook.get_cells()
        //console.log("reloading cells");
        for (var i=0; i<ncells; i++) { 
            var cell=cells[i];
            cell.render();
             }
}
init_cells();
  };
    load_ipython_extension();
    return {
        load_ipython_extension : load_ipython_extension,
	
    };
};  //End of thmInNb
run_this();
console.log("Loading ./jfb-local-thms-tools.js");
