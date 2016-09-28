#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import subprocess
import shlex
import logging
import argparse
import datetime
import os

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="BAM files", nargs='+')
parser.add_argument("-n", "--cores", help="Number of Cores to use")

args = parser.parse_args()
 

bam_files = args.input
n_cores = int(args.cores)

target = '/home/ubuntu/projects/input/bed/SureSelect_Human_Exon_V5_merge.withoutchr.bed'
human_reference = "/home/ubuntu/projects/input/grch37/d5/hs37d5.fa" #86 features
access = "/home/ubuntu/projects/input/cnvkit/access-5k-mappable.hg19.withoutchr.bed"
ref_flat = "/home/ubuntu/projects/input/cnvkit/refFlat.withoutchr.txt"

output_folder = "/home/ubuntu/projects/output/cnvkit"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

log_file = "%s/cnvkit.run.%s.log.txt" % (output_folder, str(datetime.datetime.now()).replace(' ', '_'))
# log_file = "test"
logging.basicConfig(filename=log_file,level=logging.DEBUG)

start_time = datetime.datetime.now()
logging.info("Start time: "+str(start_time))

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            # print(output.strip())
            logging.info(output.strip())
    rc = process.poll()
    return rc


command = """cnvkit.py batch %s -n -t %s -f %s \
    --access %s \
    --output-reference %s/my_flat_reference.cnn -d %s/cnvkit_run/ \
    --annotate %s \
    -p %s --diagram --scatter \
    """ % (" ".join(bam_files), target, human_reference, access, output_folder, output_folder, ref_flat, n_cores)

# run_command(command)
print command
# return x*x
for bam_file in bam_files:
    base=os.path.basename(bam_file)
    base_name = os.path.splitext(base)[0].split('.')[0]
    print(base_name)
    command = """cnvkit.py export vcf %s/cnvkit_run/%s.cns -y -i "%s" -o %s/cnvkit_run/%s.cnv.vcf""" % (output_folder, base_name, base_name, output_folder, base_name)
    # print(command)
    run_command(command)

# os.remove(bam_file)
finish_time = datetime.datetime.now()
logging.info("Finish time: "+str(finish_time))
logging.info("Time Taken: "+str(finish_time-start_time))