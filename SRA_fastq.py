
#!/usr/bin/python

import sys 
import os
import re
import subprocess

#Script to convert NCBI SRA files to FASTQ files using NCBI SRA toolkit 

def converter(SRR_list, path): 
	
	i = 0 

	length = len(SRR_list)

	os.chdir(path) # changes path to dump the fastq in the fastq directory 

	for i in range(0,length): 
		
		cmd = "fastq-dump -I --split-files --outdir . " + SRR_list[i] # converts SRA to fastq and splits up the forward and reverse reads in different files   

		subprocess.call(cmd, shell=True) # terminal command 

		i += 1


if __name__ == '__main__':

	SRR_FileNname = sys.argv[1]
	print SRR_FileNname

	with open(SRR_FileNname, 'r') as filename: # 
	
		SRR_Acc_List = [line.strip() for line in filename] # reads each line and saves it in a list 

	filename.close()

	file_pwd = sys.argv[2]
	print file_pwd

	converter(SRR_Acc_List, file_pwd)

