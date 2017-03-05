#!/usr/bin/env python

import os
import json
from collections import defaultdict

def subfile(folder,file):
	return "\\subfile{."+folder.replace("\\","/")+"/"+file+"}"

out = open("main.tex","w")

with open("./templates/options.json") as data_file:
	options = json.load(data_file)


out.write("\\documentclass[")
out.write(",".join(options["docoptions"]))
out.write("]{")
out.write(options["doctype"])
out.write("}\n\n")

for i in options["packages"]:
	out.write("\\usepackage{")
	out.write(i)
	out.write("}\n")
out.write("\n")

formatting = open("./templates/formatting.tex","r")
out.write(formatting.read())
out.write("\n")

out.write("\\begin{document}\n\n")

out.write("\\subfile{./templates/header.tex}\n\n\\begin{multicols}{2}\n\n")

filedict = defaultdict(list)
cwdchar = len(os.getcwd())

for a,b,c in os.walk(os.getcwd()+"/content"):
    for i in c:
    	if i[-3:] == "tex" :
    		filedict[a[cwdchar:]]
    		filedict[a[cwdchar:]].append(i)

filelist = []
for folder in filedict:
	files = filedict[folder]
	files.sort()
	data = ""
	for file in files:
		data += subfile(folder,file) + "\n"
	filelist.append(data)

filelist.sort()

for i in filelist:
	out.write(i)
	out.write("\n")

out.write("\\end{multicols}\n\n\\subfile{./templates/footer.tex}\n\n")

out.write("\\end{document}\n")