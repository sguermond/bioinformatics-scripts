  GNU nano 2.0.9                                                                                                                                                                                                File: /home/zoo/guermons/lab/Scripts/ortho_filtering.py                                                                                                                                                                                                                                                                                                                                                                                                       

#!/usr/bin/env python2.7

# this script outputs a .end file of orthologs containing only the required distribution of taxa 
# from the .end output file of FastOrtho

# Sarah Guermond
# last updated 11 July 2014

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
    print "\nIn cases where only orthologs from one list are desired, enter None for the other number"
    quit()

orthologs = sys.argv[1]
output = sys.argv[2]
list1_file = sys.argv[3]
min1 = sys.argv[4]
list2_file = sys.argv[5]
min2 = sys.argv[6]

# read lists into memory
def file_to_list(file):
    list = []
    list_handle = io.open(file, "rb")
    for line in list_handle:
        word = line.strip()
        list.append(word)
    list_handle.close()
    return(list)

list1 = file_to_list(list1_file)
list2 = file_to_list(list2_file)

# creat filehandles 
ortho_handle = io.open(orthologs, "rb")
outfile_handle = io.open(output, "wb")
seqnum_handle = io.open(output + "_seqnums", "wb")

# make function dealing with none
def none_list(inhandle, outhandle, numhandle, list_none, list_num, min):
    match = 0
    nomatch = 0
    numhandle.write("Ortholog\t" + "\t".join(list_num))
    for line in inhandle:
        sp_dict = {} # keeps track of which species have been seen in this ortholog
        list_num_count = 0
        list_none_count = 0
        line_list = line.strip().split("\t")
        seq_line = line_list[1].strip()
        seq_species = seq_line.split(" ")
        for seq_sp in seq_species:
            left = seq_sp.find('(')
            right = seq_sp.find(')')
            sp = seq_sp[left+1:right]
            if sp in list_num:
                # check if seen before
                if sp in sp_dict:
                    sp_dict[sp] += 1
                else:
                    sp_dict[sp] = 1
                    list_num_count += 1
            elif sp in list_none:
                list_none_count += 1
            else:
                print "No species ", sp, " found in none list"
        # check against requirements
        if list_num_count >= min and list_none_count == 0:
            outhandle.write(line)
            # get ortholog name 
            ortho_header = line_list[0]
            ortho_header_split = ortho_header.split(" ")
            ortho = ortho_header_split[0]
            match += 1
            # print to seq num file
            numhandle.write('\n' + ortho + '\t')
            for species in list_num:
                if species in sp_dict:
                    numhandle.write((str(sp_dict[species]) + "\t").rstrip('\n'))
                else:
                    numhandle.write((str("0") + '\t').rstrip('\n'))
        else:
            nomatch += 1
    return(match, nomatch)

# if no None
def regular_list(inhandle, outhandle, numhandle, list1, min1, list2, min2):
    match = 0
    nomatch = 0
    numhandle.write("Ortholog\t" + "\t".join(list1 + list2))
    for line in inhandle:
        sp_dict = {} # keeps track of which species have been seen in this ortholog
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
                if sp in sp_dict:
                    sp_dict[sp] += 1
                else:
                    sp_dict[sp] = 1
                    list1_count += 1
            elif sp in list2:
                if sp in sp_dict:
                    sp_dict[sp] += 1
                else:
                    sp_dict[sp] = 1
                    list2_count += 1
            else:
                print "No species ", sp, " found in list 1 or 2"
        if list1_count >= min1 and list2_count >= min2:
            # print line to outfile
            outhandle.write(line)
            # get ortholog name 
            ortho_header = line_list[0]
            ortho_header_split = ortho_header.split(" ")
            ortho = ortho_header_split[0]
            # print to seq num file
            numhandle.write('\n' + ortho + '\t')
            for species in list1 + list2:
                if species in sp_dict:
                    numhandle.write((str(sp_dict[species]) + "\t").rstrip('\n'))
                else:
                    numhandle.write((str("0") + '\t').rstrip('\n'))
            match += 1
        else:
            nomatch += 1
    return(match, nomatch)

# establish number needed for list
if min1 == "None" and min2 != "None":
    num2 = int(min2)
    match, nomatch = none_list(ortho_handle, outfile_handle, seqnum_handle, list1, list2, num2)
elif min2 == "None" and min1 != "None":
    num1 = int(min1)
    match, nomatch = none_list(ortho_handle, outfile_handle, seqnum_handle, list2, list1, num1)
elif min1 == min2 == "None":
    print "Error: you asked for none from both lists"
    quit()
else:
    num1 = int(min1)
    num2 = int(min2)
    match, nomatch = regular_list(ortho_handle, outfile_handle, seqnum_handle, list1, num1, list2, num2)

print match, " matches found"
print nomatch, " had no matches"

ortho_handle.close()
outfile_handle.close()


