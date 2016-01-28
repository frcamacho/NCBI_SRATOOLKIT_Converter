# -*- coding: utf-8 -*-
"""
Created on Thursday Jan 28 12:01:12 2016

@author: francinecamacho
"""
from multiprocessing import Process 
import sys 
import os
import re
import subprocess

def sra_To_Fastq(sra_dir_path, outdir_path): 
	
# changes path to dump the fastq in the fastq directory 

	for sraFile in os.listdir(sra_dir_path):
		
		newprocess = Process(target=convertSRA_to_fastq,args=(sraFile,sra_dir_path,outdir_path,))
		newprocess.start()
		newprocess.join()

def convertSRA_to_fastq(sraFile, sra_dir_path, outdir_path):
	sraName = sraFile.split(".")[0]
		
	cmd = "fastq-dump -A "+ sraName + " " + sra_dir_path +"/"+ sraFile + " -I --split-files --outdir " + outdir_path # converts SRA to fastq and splits up the forward and reverse reads in different files   
	print cmd 
	subprocess.call(cmd, shell=True) # terminal command 

def main(sra_dir_path, sra_dir_folder, outdir_path, outdir_folder): 
	os.chdir(sra_dir_path)
	sra_dir_path = os.path.join(sra_dir_path, sra_dir_folder)
	outdir_path = os.path.join(outdir_path, outdir_folder)
	os.mkdir(outdir_path)
	sra_To_Fastq(sra_dir_path, outdir_path)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--sra_dir_path', type= str, required=True)
	parser.add_argument('--sra_dir_folder', type= str, required=True)
	parser.add_argument('--outdir_path', type=str, required=True)
	parser.add_argument('--outdir_folder', type=str, required=True)

	args = parser.parse_args()

	main(args.sra_dir_path, args.sra_dir_folder, args.outdir_path, args.outdir_folder)
