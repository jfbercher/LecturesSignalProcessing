from IPython.html import widgets
from IPython.display import clear_output, display, HTML, Image, Javascript
# From http://nbviewer.ipython.org/gist/anonymous/840b5cec9e19f3e39090
hbox = lambda x: (x.remove_class("vbox"), x.add_class("hbox"))
#
frame = lambda x: x.set_css({
    "border": "outset 1px",
    "padding": 5,
    "border-radius": 5,
    "display": "inline-box",
    "margin": "5px"
})

# Example
if __name__=="__main__":
    c = widgets.CheckboxWidget(description="", value=True)#, width=100, font_size='14pt', fore_color='red')
    t = widgets.HTMLWidget(value="how solution with a very long text how to align on the left? how solution with a very long text how to align on the left? how solution with a very long text how to align on the left?")
    t.set_css({'font-size': 16, 'width':'80%', 'margin-top':4})
    cont = widgets.ContainerWidget(children=[c,t])

    frame(cont)
    display(cont)
    _=hbox(cont)