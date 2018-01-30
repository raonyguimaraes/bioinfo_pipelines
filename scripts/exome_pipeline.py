import os

from subprocess import run, check_output
fastqs = ['ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR098/SRR098401/SRR098401_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR098/SRR098401/SRR098401_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/004/SRR1517974/SRR1517974_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/004/SRR1517974/SRR1517974_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/003/SRR1518043/SRR1518043_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/001/SRR1517991/SRR1517991_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517938/SRR1517938_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/001/SRR1517991/SRR1517991_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/001/SRR1518011/SRR1518011_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/002/SRR1518192/SRR1518192_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/006/SRR1517906/SRR1517906_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/004/SRR1518044/SRR1518044_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517968/SRR1517968_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/004/SRR1518044/SRR1518044_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/003/SRR1518133/SRR1518133_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/003/SRR1518253/SRR1518253_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1518158/SRR1518158_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517848/SRR1517848_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/004/SRR1517884/SRR1517884_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/006/SRR1517906/SRR1517906_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517938/SRR1517938_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517878/SRR1517878_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1518158/SRR1518158_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517848/SRR1517848_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/001/SRR1518011/SRR1518011_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/003/SRR1518043/SRR1518043_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517968/SRR1517968_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/004/SRR1517884/SRR1517884_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/007/SRR1518197/SRR1518197_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/002/SRR1518192/SRR1518192_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/003/SRR1518133/SRR1518133_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/003/SRR1518253/SRR1518253_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/007/SRR1518197/SRR1518197_1.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/008/SRR1517878/SRR1517878_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/001/SRR1518151/SRR1518151_2.fastq.gz', 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR151/001/SRR1518151/SRR1518151_1.fastq.gz']

h_reference = 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.15_GRCh38/seqs_for_alignment_pipelines.ucsc_ids/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz'

# def download_files():
os.chdir('input')

def main():
	download_fastqs()

def download_fastqs():

	for fastq in fastqs:
		command = 'wget {}'.format(fastq)
		run(command, shell=True)

def index_bwa():
	command = '../../programs/bwa/bwa index GCA_000001405.15_GRCh38_no_alt_analysis_set.fna'

def install_bwa():
	command = 'sudo apt install bwa'


def install_minimap():
	command = 'curl -L https://github.com/lh3/minimap2/releases/download/v2.7/minimap2-2.7_x64-linux.tar.bz2 \
	| tar -jxvf - \
	./minimap2-2.7_x64-linux/minimap2'

main()
