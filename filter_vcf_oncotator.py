#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import subprocess
import shlex
import logging
import argparse
import datetime
import os

from subprocess import call

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="VCF file")

args = parser.parse_args()
 
vcf_file = args.input

base=os.path.basename(vcf_file)
base_name = os.path.splitext(base)[0]


gvcftools_path = "/home/ubuntu/projects/programs/gvcftools-0.16/bin"
vcftools_path = "/home/ubuntu/projects/programs/vcftools/vcftools-0.1.14/src"
bcftools_path = "/home/ubuntu/projects/programs/bcftools/bcftools-1.3.1"
snpeff_path = "/home/ubuntu/projects/programs/snpeff/snpEff"

#/home/ubuntu/projects/programs/vcftools/vcftools-0.1.14/src/cpp/
#/home/ubuntu/projects/programs/vcftools/vcftools-0.1.14/src/perl/

#extract vcf from gvcf
print('extract vcf from gvcf')
#gzip -dc ../../input/WGC081270U.g.vcf.gz | ../../programs/gvcftools-0.16/bin/extract_variants | bgzip -c > WGC081270U.vcf.gz
command = """cat %s | %s/extract_variants > %s.variants.vcf""" % (vcf_file, gvcftools_path, base_name)
output = call(command, shell=True)
print(output)