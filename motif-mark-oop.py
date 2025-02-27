#!/usr/bin/env python

import math
import cairo
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("-m", help="motif list file") #type: str
    parser.add_argument("-f", help="fasta file") #type: str
    parser.add_argument("-o", help="output fig prefex") #type: str
    return parser.parse_args()

args = get_args()

motif = args.m 
fasta = args.f 
comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C','N': 'N', 'a':'t', 't':'a', 'c':'g', 'g':'c', 'n':'n'}

#define function to reverse compliment 
def rev_comp(seq: str) -> str:
    '''this function returns a reverse copliments a sequence of upper case bases including Ns'''
    rev_seq = seq[::-1]
    RC = ""
    for base in rev_seq: 
        RC += comp_dict[base]
    return(RC)

# define the motif  class 
# will hold the motif and have a function to generate the possible variations
# color assigned to that motif 
# list of start locations for that motif
class MotifSeq: 
    def __init__(self, motif):
        self.motif = motif

# define fasta record class 
# hold  holds the intron and exon locations 
# hold total length of record
# hold header 
class record:
    def __init__(self, intron_start, intron_end, exon_start, exon_end, total_len):
        self.intron_start = intron_start
        self.intron_end = intron_end
        self.exon_start = exon_start
        self.exon_end = exon_end
        self.total_len = len(self)

# open the fasta file and read in the fasta records: 

with (open(fasta, "r") as fasta):
    header = ''
    seq = ''
    intron_start = 0
    exon_loc = []
    for line in fasta: 
        #set the header and seq variables equal to the header and seq of that record 
        if line.startswith(">"):
            header = line.strip()
        else: 
            seq += line.strip()
        # reverse compliment the sequence if needed 
        if "reverse complement" in header: 
            seq = rev_comp(seq)
            # print(seq)
        elif "reverse complement" not in header: 
            seq = seq
        #find exon location
        for i, character in enumerate(seq):
            # print(seq)
            # print(i)
            # print(character)
            if character.isupper() == True:
                # print("exon found")
                # print(header)
                # print(character)
                # print(i)
                exon_loc.append(i)

            # print(exon_loc)
                exon_start = exon_loc[0]
                exon_end = exon_loc[-1]
                print(header)
                print(exon_start)
                print(exon_end)

            # elif c


        


