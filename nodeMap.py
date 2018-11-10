from __future__ import print_function
import sys

torusDict = {
	"a" : ["b","m","d","e"],
	"b" : ["c","n","a","f"],
	"c" : ["d","o","b","g"],
	"d" : ["a","p","c","h"],
	"e" : ["f","a","h","i"],
	"f" : ["g","b","e","j"],
	"g" : ["h","c","f","k"],
	"h" : ["e","d","g","l"],
	"i" : ["j","e","l","m"],
	"j" : ["k","f","i","n"],
	"k" : ["l","g","j","o"],
	"l" : ["i","h","k","p"],
	"m" : ["n","i","p","a"],
	"n" : ["o","j","m","b"],
	"o" : ["p","k","n","c"],
	"p" : ["m","l","o","d"]
}

torusList = [
	["b","m","d","e"],
	["c","n","a","f"],
	["d","o","b","g"],
	["a","p","c","h"],
	["f","a","h","i"],
	["g","b","e","j"],
	["h","c","f","k"],
	["e","d","g","l"],
	["j","e","l","m"],
	["k","f","i","n"],
	["l","g","j","o"],
	["i","h","k","p"],
	["n","i","p","a"],
	["o","j","m","b"],
	["p","k","n","c"],
	["m","l","o","d"],
]

print(torusList)

torus = [[0 for x in range(16)] for y in range(16)]
'''
torusTuple = (tuple(tuple((ord(node) - 97) for node in torusDict[nodeList]) for nodeList in torusDict))
torusTupleChar = (tuple(tuple((node) for node in torusDict[nodeList]) for nodeList in torusDict))
print(torusTupleChar)
print(torusTuple)
'''

for i in range(len(torus)):
	for j in range(len(torus)):
		# print(chr(j+97) + " : " + str(torusList[i]))
		if chr(j+97) in torusList[i]:
			#print(str(j) + " is in " + str(torusList[j]))
			torus[i][j] = 1
	print(torus[i])

'''

a	b	c	d

e	f	g	h

i	j	k	l

m	n	o	p


* graph is undirected, but (p,l) implies p --> l
* x[0/1/2/3] = right/north/left/south

'''