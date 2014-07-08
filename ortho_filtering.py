#!/usr/bin/env python2.7

# this script outputs a .end file of orthologs containing only the required distribution of taxa 
# from the .end output file of FastOrtho

# Sarah Guermond
# 8 July 2014

import io
import sys
import re
import os
from collections import defaultdict

if len(sys.argv) < 6:
	print("\nProduces filtered .end file (FastOrtho) with the required number of matches")
	print "from two user-specified categories"
	print("\nUsage: ./ortho_filtering.py <ortho.end> <output> <list 1> <num 1> <list 2> <num 2>")
	print("\n\t<ortho.end>: FastOrtho .end file")
	print("\t<list 1>: list of species in category 1 (must match species names in .end)")
	print("\t<num 1>: minimum number of representatives from list 1 desired in ortholog")
	print("\t<list 2>: list of species in category 2 (must match species names in .end)")
	print("\t<num 2>: minimum number of representatives from list 2 desired in ortholog")
	print("\nEx: ./ortho_filtering.py orthos.end filtered_orthos.end cats.txt 2 dogs.txt 3")
	print "will return orthologs with at least 2 cats and 3 dogs"
	quit()

orthologs = sys.argv[1]
output = sys.argv[2]
list1_file = sys.argv[3]
min1 = int(sys.argv[4])
list2_file = sys.argv[5]
min2 = int(sys.argv[6])

# read lists into memory
list1 = []
list1_handle = io.open(list1_file, "rb")
for line in list1_handle:
	sp = line.strip()
	list1.append(sp)

list2 = []
list2_handle = io.open(list2_file, "rb")
for line in list2_handle:
	sp = line.strip()
	list2.append(sp)

list1_handle.close()
list2_handle.close()

ortho_handle = io.open(orthologs, "rb")
outfile_handle = io.open(output, "wb")

match = 0
nomatch = 0

for line in ortho_handle:
	list1_count = 0
	list2_count = 0
	line_list = line.strip().split("\t")
	seq_line = line_list[1].strip()
	seq_species = seq_line.split(" ")	
	for seq_sp in seq_species:
		# split on ()
		left = seq_sp.find('(')
		right = seq_sp.find(')')
		sp = seq_sp[left+1:right]
		if sp in list1:
			list1_count += 1
		elif sp in list2:
			list2_count += 1
		else:
			print "No species ", sp, " found in list 1 or 2"		
	if list1_count >= min1 and list2_count >= min2:
		# print line to outfile
		outfile_handle.write(line)
		match += 1
	else:
		nomatch += 1

print match, " matches found"
print nomatch, " had no matches"
		
ortho_handle.close()
outfile_handle.close()
