#!/usr/bin/env python2.7

# this script creates fasta files of protein or nucleotide sequences 
# from the .end output file of FastOrtho

# Sarah Guermond
# 18 June 2014

import io
import sys
import re
import os
from collections import defaultdict
from Bio import SeqIO

if len(sys.argv) < 5:
	print("\n\tThis script creates fasta files of protein or nucleotide sequences")
	print("\tfrom the .end output file of FastOrtho.")
	print("\n\tUsage: ./ortho_end_to_fasta.py <ortho.end> <in format> <list>")
	print("\n\t<ortho.end>: FastOrtho .end file")
	print("\t<in format>: file extension of FastOrtho input file (pep, fasta...)")
	print("\t<num taxa>: minimum number of taxa  desired in ortholog")
	print("\t<list>: tab-separated list of reference nuc/pep files, FastOrtho input file, and species prefix")
	print("\t\tEx: \tDuncanopsammia_longest.cds\tDaxi.transdecoder.pep\tDaxi\n")
	quit()

orthologs = sys.argv[1]
extension = sys.argv[2]
min_taxa = sys.argv[3]
info_file_list = sys.argv[4]

### to do: automatically move new fasta files to new dir
# make new dir ortho_fasta to create fasta files in
# os.makedirs("ortho_fasta")
# change | to _ for Clustal processing

# read list of species info
#### reference	transdecoder	species
info_handle = io.open(info_file_list, "rb")
info_files = []
info = {}

for line in info_handle:
	info_files_list = line.strip().split("\t")
	info = {"ref_file": info_files_list[0], "fo_file": info_files_list[1], "species_prefix": info_files_list[2]}
	info_files.append(info)
info_handle.close()

# dictionary: species.seqname -> ortholog
ortho_handle = io.open(orthologs, "rb")
species_seqname_to_ortho = {}
for line in ortho_handle:
        # get number of taxa
        line_list = line.strip().split("\t")
        ortho_header = line_list[0]
        ortho_header_split = ortho_header.split(" ")
        gene_taxa = ortho_header_split[2]
        num_taxa_result = re.subn("genes,", "", gene_taxa, 0)
        num_taxa_split = num_taxa_result[0].strip().split(" ")
        num_taxa = num_taxa_split[0]
        # skip to next if too few taxa in ortholog
        if num_taxa < min_taxa:
                continue

        # get ortholog name
        ortho = ortho_header_split[0]

	# get species filenames, seqs
	seq_line = line_list[1].strip()
	seq_species = seq_line.split(" ")	
	for seq_sp in seq_species:		
		result = re.subn("[\(\)]", " ", seq_sp, 0)
		seq_sp_split = result[0].strip().split(" ")
		seq_name = seq_sp_split[0]
		species_file = seq_sp_split[1] + "." + extension

		# search info_list for same FastOrtho file to get species
		item_info = (item for item in info_files if item["fo_file"] == species_file).next()	
		# make key		
		species_seq = item_info['species_prefix'] + "." + seq_name
		species_seqname_to_ortho[species_seq] = ortho
ortho_handle.close()

# for seq in reference file
for species in info_files:
	infile = open(species['ref_file'], "rU")
	for record in SeqIO.parse(infile, "fasta"):
		# get seqname
		seqid_raw = record.id
		seqid_list = seqid_raw.strip().split('\s')
		seqid = seqid_list[0]
		seq = str(record.seq)
		# recover species.seqname
		species_seqname = species['species_prefix'] + "." + seqid
		# find it in the dictionary, get associated ortholog
		if species_seqname in species_seqname_to_ortho:
			ortho = species_seqname_to_ortho.get(species_seqname)
			with open(ortho + '.fasta', 'a') as outfile:
				outfile.write('>' + species['species_prefix'] + '_' + seqid + '\n' + seq + '\n')
