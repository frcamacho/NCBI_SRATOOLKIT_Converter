# NCBI_SRATOOLKIT_Converter
----------------------------------------------------------------------

####Francine Camacho 

####+Requirements: 

1. NCBI SRA TOOLKIT (http://www.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=show&f=software&m=software&s=software)

----------------------------------------------------------------------

####Setting up the pipeline: 

#####Using a SRR Accession list to convert SRA files to fastq format
#####the pipeline consists of three sequential steps: 

1. The first step is to download the Accession List (list of SRR IDs 
or IDs of raw sequence runs). To do so, search for the BioProject,
BioStudy, Biosample, SRA Experiment accession numbers in the search 
bar from the SRA locater website 
(http://trace.ncbi.nlm.nih.gov/Traces/study/?go=home). Then click on 
“Accession List” button. 

2. The second step is to convert SRA data into fastq format. Run the 
'SRA_fastq.py' script in the directory with the following parameters:

python  ./SRA_fastq.py SRR_ACC_LIST OUT_FASTQ_FILES_DIR 

SRR_ACC_LIST: file with SRR accession numbers (if file is in 
			  another directory just use the 
			  path to the file)

OUT_FASTQ_FILES_DIR: directory where to store the converted 
		          fastq files 


3. The third step is to take the the fastq files and convert to 
FASTA format. Run the ‘fastq_to_fasta.py’ script in the 
directory with the following parameters:

python ./fastq_to_fasta.py FASTQ_FILES_DIR OUT_FASTA_FILES_DIR

FASTQ_FILES_DIR: directory where fastq files are stored 

OUT_FASTA_FILES_DIR: directory where to store converted fasta files 


#####Using SRA files downloaded from the NCBI to convert to fastq format
#####the pipeline consist of two steps: 

1. The first step is to convert SRA data into fastq format. Run the 
‘localSRA.py’ script in the directory with the following parameters:

python  ./localSRA.py SRA_DIR OUT_FASTQ_FILES_DIR 

SRA_DIR: directory containing SRA files from NCBI

OUT_FASTQ_FILES_DIR: directory where to store the converted 
		          fastq files 


2. The third step is to take the the fastq files and convert to 
FASTA format. Run the ‘fastq_to_fasta.py’ script in the 
directory with the following parameters:

python ./fastq_to_fasta.py FASTQ_FILES_DIR OUT_FASTA_FILES_DIR

FASTQ_FILES_DIR: directory where fastq files are stored 

OUT_FASTA_FILES_DIR: directory where to store converted fasta files  





