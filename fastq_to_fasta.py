
#!/usr/bin/python

import sys
import os
import re
import subprocess

#Script to convert FASTQ files to FASTA files

def FastqToFasta(path): 
	
	# base = os.path.basename(path+fastq_filename)

	# SRR_name = os.path.splitext(base)[0]+ ".fa"
	os.chdir(path) 
	SRR_list =[]

	for fastq_files in os.listdir(path):
		base = fastq_files.split("_")
		SRR_name = base[0]
		
		if SRR_name in SRR_list: 
			continue 

		else: 

			SRR_list.append(SRR_name)
			#fastq files are split into two files so we need to merge them to create a fasta file. 
			cmd = "fq2fa --merge --filter " + SRR_name +"_1.fastq " + SRR_name +"_2.fastq " + SRR_name + ".fa" 

			print cmd

			subprocess.call(cmd, shell=True)

if __name__ == '__main__':

	FASTQSOURCE = sys.argv[1]
	
	FastqToFasta(FASTQSOURCE)
