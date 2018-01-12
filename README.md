# ApeShape
### A Project endeavors to find the ancestral states of genetics variants provided by database.

## Please cite our work -- here is the ICMJE Standard Citation:
### ...and a link to the DOI:

![alt text](https://i.pinimg.com/736x/c7/9e/77/c79e77061058fe2f14bb22225be441a1.jpg)

## Intro statement
This pipeline finds ancestral states of each polymorphic site in clinVar. In addition, it finds the frequency at which these polymorphisms occur in the population, using data from the 1000 Genomes project as a proxy for this information. 

# Workflow
![alt text](https://github.com/NCBI-Hackathons/PrimateAncestralAlleles/blob/master/workflow.png?raw=true)

#Implementation
#Data Preparation

The data preparation process is accomplished through one R.script file named ‘Data_Processing’. If the user is using the .vcf file which is downloaded from the NCBI the R.script will automatically get the chromosome number and the position of SNPs and calculated the start and ending positions of the sequence. A .bed file would be output by the R.script which will be used to find the sequences.

The bed file will be upload to Genome Browser. Use link https://genome.ucsc.edu/cgi-bin/hgCustom to upload the file. Using the USCS table browser, we extracted the sequences at the position of the variants +/- 75 bases. 

The information extraction from .vcf file downloaded from NCBI are still under development. Since not all SNPs in .vcf file have IDs associated with them, now the R.script will successfully extract the Allele ID for each SNP.

#BLAST (Align the human sequence with 4 other primates) (Need Help)

A custom BLAST database composed of the reference genomes for Human, Chimp, Gorilla, orangutan and macaque monkeys (change this part later) was used to find the sequences described above for each of the different ancestral species. A blastn search was performed in order to do this. 

#Phangorn (Compute the most probable ancestral allele) (Need Help)

The R package Phangorn was used to compute the ancestral allele state in these sequences. This is done by providing a phylogenetic tree and the sequences to the R package. It then produces a maximum likelihood estimate of the ancestral allele.

# How to use <this software>
![alt tag](https://socalhack2018.slack.com/messages/C8H3T34BG/details/)

# Deliverables

A file containing the ancestral state and allele frequency for all clinVar variants that can be found in the 1000 Genomes data. Otherwise, the allele frequency will not be included, only the ancestral state.
  
