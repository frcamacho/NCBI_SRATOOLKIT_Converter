
#!/usr/bin/python

import sys
import os
import re
import subprocess

#Script to convert NCBI SRA files on a local computers to FASTQ files using NCBI SRA toolkit 

def converter(sraPath, outDirPath): 
	
# changes path to dump the fastq in the fastq directory 

	for sra_File in os.listdir(sraPath):

		if sra_File != ".DS_Store": 
			sraNameList = sra_File.split(".")
			sraName = sraNameList[0]
		
			cmd = "fastq-dump -A "+ sraName + " " + sraPath + sra_File + " -I --split-files --outdir " + outDirPath # converts SRA to fastq and splits up the forward and reverse reads in different files   
			print cmd 
			subprocess.call(cmd, shell=True) # terminal command 


if __name__ == '__main__':

	FILE_PWD = sys.argv[1]
	#'/molbio2/labs/donialab/fcamacho/Mohamed_SRA_files/'
	OUTFILE_PWD = sys.argv[2]
	#'/molbio2/labs/donialab/fcamacho/Sediment_metatranscriptomic_Orsi/'

	converter(FILE_PWD, OUTFILE_PWD)

