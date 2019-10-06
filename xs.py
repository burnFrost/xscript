#!/usr/bin/env python3
#xscript


xscript = ""

result = ""

cppsrc = ""

pysrc = ""



#setup
cpp_start = """#include <iostream>
"""



cpp_exit = """
return 0;}"""

py_start = """#!/usr/bin/env python3
"""


#syntax

xbool = "vbool "
xint = "vint "
xfloat = "vfloat "
xstring = "vstring "
defbool = "vdef "
defint = "dint "
deffloat = "dfloat "
defstring = "dstring "
defvoid = "dvoid "

cpp = [
["xmain", "int main"],
["xns", "using namespace"],
[xbool, "bool "],
[xint, "int "],
[xfloat, "float "],
[xstring, "string "],
[defbool, "bool "],
[defint, "int "],
[deffloat, "float "],
[defstring, "string "],
[defvoid, "void "],
["):\n", "){\n"],
[":;", "}"],
["True", "true"],
["False", "false"],
["xin>\n", "getline(cin, "],
["</xin", ");"],
["xout>", "cout << "],
["</xout", " << endl;"],
["class>", "class "],
["</class", "{\n	public:"],
["py: ", "//"],
["cpp: ", ""],
["list[", "{"],
["/]", "}"],
["object>", ""],
["</object", ""],
["<new>", " "],
["</new>", ";//"]
]



py = [
["xmain", "#"],
["xns", "#"],
[xbool, ""],
[xint, ""],
[xfloat, ""],
[xstring, ""],
[defbool, "def "],
[defint, "def "],
[deffloat, "def "],
[defstring, "def "],
[defvoid, "def "],
[":;", ""],
[";", ""],
["true", "True"],
["false", "False"],
["xin>", ""],
["</xin", " = input()"],
["xout>", "print("],
["</xout", ")"],
["class>", "class "],
["</class", ":"],
["py: ", ""],
["cpp: ", "#"],
["list[", "["],
["/]", "]"],
["object>", "#"],
["</object", ""],
["<new>", "\n"],
["</new>", " = "]
]






#functions


def convert(code, syntax):
	for x in range(0, len(code)):
		for x in range(0, len(syntax)):
			code = code.replace(syntax[x][0],syntax[x][1])
	return code


#openfile
filename = input("File: ")
xfile = open(filename+".xs","r")
xscript = xfile.read()

#xscript
cppsrc = xscript
pysrc = xscript


#convert
cppsrc = convert(cppsrc, cpp)
pysrc = convert(pysrc, py)


#setup+src
cppsrc = cpp_start+cppsrc+cpp_exit
pysrc = py_start+pysrc


#savefiles
cppfile = open(filename+".cpp","w")
pyfile = open(filename+".py","w")

cppfile.write(cppsrc)
pyfile.write(pysrc)


print(xscript)

#closefiles
xfile.close()

cppfile.close()
pyfile.close()


