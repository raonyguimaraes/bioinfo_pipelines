#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import subprocess
import shlex
import logging
import argparse
import datetime

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

output = "/home/ubuntu/projects/output/cnvkit"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

log_file = "%s/cnvkit.run.%s.log.txt" % (output, str(datetime.datetime.now()))

logging.basicConfig(filename=log_file,level=logging.DEBUG)

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

# command = "python cnvkit.py -i %s" % (bam_file)

command = """cnvkit.py batch %s -n -t %s -f %s \
    --access %s \
    --output-reference %s/my_flat_reference.cnn -d %s/cnvkit_run/ \
    --annotate %s \
    -p %s --diagram --scatter \
    """ % (" ".join(bam_files), target, human_reference, access, output, output, ref_flat, n_cores)

run_command(command)
print command
# return x*x
