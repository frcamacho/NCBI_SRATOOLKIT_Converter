# NCBI_SRATOOLKIT_Converter
----------------------------------------------------------------------

####Francine Camacho 

####+Requirements: 

1. NCBI SRA TOOLKIT (http://www.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=show&f=software&m=software&s=software)

2. A basic knowledge of NCBI SRA TOOLKIT

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

python ./SRA_fastq.py --sra_dir_path DATA_PATH --sra_dir_folder SRA_FOLDER --outdir_path OUTPATH --outdir_folder OUTDIR_FOLDER 

DATA_PATH: The root directory path to where SRA folder is contained
			  
SRA_FOLDER: Name of directory which contains SRA files 

OUTPATH: Directory path where you want to output OUTDIR_FOLDER 

OUTDIR_FOLDER: Name of directory you want to make to contain the
		convert sra files which are now in FASTQ format 


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





