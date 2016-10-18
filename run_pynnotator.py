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
parser.add_argument("-o", "--output", help="Output folder")


args = parser.parse_args()
 
vcf_file = args.input
output = args.output

if not os.path.exists(output):
    os.makedirs(output)

os.chdir(output)

base=os.path.basename(vcf_file)
base_name = os.path.splitext(base)[0]


#clean_nonref
vcf_reader = open(vcf_file)
vcf_writer = open("%s.pynnotator.vcf" % (base_name), 'w')
for line in vcf_reader:
    # print(line)
    if line.startswith("#"):
        vcf_writer.writelines(line)
    else:
        variant = line.split('\t')
        alt = variant[4].split(',')
        new_alt = []
        for item in alt:
            if item != '<NON_REF>':
                new_alt.append(item)
        # alt = alt.replace(',<NON_REF>', '')
        alt = ','.join(new_alt)
        variant[4] = alt
        #check genotypes
        genotype = variant[-1].split(':')[0]
        print(genotype)

        vcf_writer.writelines("\t".join(variant))


vcf_writer.close()

# command = 'pynnotator -i %s' % (vcf_file)
# output = call(command, shell=True)
# print(output)
