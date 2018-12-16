import sys, re

filename = sys.argv[1]
with open(filename, 'r') as f:
    text = f.read()
    back = re.findall(r"\[Back\]\(([\S\s]*?)\)", text)[0].replace("ipynb","html")
    next = re.findall(r"\[Next\]\(([\S\s]*?)\)", text)[0].replace("ipynb","html")
    index = re.findall(r"\[Index\]\(([\S\s]*?)\)", text)[0].replace("ipynb","html")

print('&lt; <a href="{0}" title="{0}"> previous </a> | <a href="{1}" title="{1}"> index </a> | <a href="{2}" title="{2}"> next </a> &gt;'.format(back, index, next))

