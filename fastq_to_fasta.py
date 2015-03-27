
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

		# cmd = "fq2fa --merge --filter " + fastq_filename + " "+ SRR_name # if the forward and reverse reads are combined in one fastq file 
		
		# print cmd
			SRR_list.append(SRR_name)

			cmd = "fq2fa --merge --filter " + SRR_name +"_1.fastq " + SRR_name +"_2.fastq " + SRR_name + ".fa" #fastq files are split into two files so we need to merge them to create a fasta file. 

			print cmd

			subprocess.call(cmd, shell=True)




if __name__ == '__main__':

	FASTQSOURCE = sys.argv[1]

	#"/molbio2/labs/donialab/fcamacho/fastq_files/"
	
	FastqToFasta(FASTQSOURCE)












